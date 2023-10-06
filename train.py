import argparse
import os
import warnings

import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from tqdm import tqdm

import models
from config import Config
from dataset import dataloader
from models.res_unet import ResUnet
from models.res_unet_plus import ResUnetPlusPlus
from utils import metrics
from utils import utils
from utils.logger import MyWriter

warnings.simplefilter("ignore", (UserWarning, FutureWarning))


# hp: 超参数
def main(hp, num_epochs, resume, name):
    checkpoint_dir = "{}/{}".format(hp.checkpoints, name)
    os.makedirs(checkpoint_dir, exist_ok=True)

    os.makedirs("{}/{}".format(hp.log, name), exist_ok=True)
    writer = MyWriter("{}/{}".format(hp.log, name))
    # get model

    if hp.MODEL == 'ResUnetPlusPlus':
        model = ResUnetPlusPlus(3).cuda()
    elif hp.MODEL == 'ResUnet':
        model = ResUnet(3).cuda()
    else:
        model = models.__dict__[hp.MODEL](num_classes=args.num_classes, output_stride=args.output_stride)
        if args.separable_conv and 'plus' in hp.MODEL:
            models.convert_to_separable_conv(model.classifier)
        utils.set_bn_momentum(model.backbone, momentum=0.01)
        model.cuda()
    # print(model)

    # set up binary cross entropy and dice loss
    criterion = metrics.BCEDiceLoss()

    # optimizer
    # optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=momentum, nesterov=True)
    # optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-5)
    optimizer = torch.optim.Adam(model.parameters(), lr=hp.lr)

    # decay LR
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1)

    # starting params
    best_loss = 999
    start_epoch = 0
    # 断点续训
    if resume:
        if os.path.isfile(resume):
            print("=> loading checkpoint '{}'".format(resume))
            checkpoint = torch.load(resume)

            start_epoch = checkpoint["epoch"]

            best_loss = checkpoint["best_loss"]
            model.load_state_dict(checkpoint["state_dict"])
            optimizer.load_state_dict(checkpoint["optimizer"])
            print(
                "=> loaded checkpoint '{}' (epoch {})".format(
                    resume, checkpoint["epoch"]
                )
            )
        else:
            print("=> no checkpoint found at '{}'".format(args.resume))

    # get data
    mass_dataset_train = dataloader.ImageDataset(
        hp, transform=transforms.Compose([dataloader.ToTensorTarget()])
    )

    mass_dataset_val = dataloader.ImageDataset(
        hp, False, transform=transforms.Compose([dataloader.ToTensorTarget()])
    )

    # creating loaders
    train_dataloader = DataLoader(
        mass_dataset_train, batch_size=hp.batch_size, num_workers=2, shuffle=True
    )
    val_dataloader = DataLoader(
        mass_dataset_val, batch_size=1, num_workers=2, shuffle=False
    )

    step = 0
    for epoch in range(start_epoch, num_epochs):

        # step the learning rate scheduler
        lr_scheduler.step()

        # run training and validation
        # logging accuracy and loss
        train_acc = metrics.MetricTracker()
        train_loss = metrics.MetricTracker()
        # iterate over data

        loader = tqdm(train_dataloader, desc=f"training Epoch {epoch + 1}/{args.epochs}")

        for idx, data in enumerate(loader):

            # get the inputs and wrap in Variable
            inputs = data["sat_img"].cuda()
            # labels.Size([16, 1, 256, 256])
            labels = data["map_img"].cuda()

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward
            # prob_map = model(inputs) # last activation was a sigmoid
            # outputs = (prob_map > 0.3).float()
            # outputs.Size([16, 1, 256, 256])
            outputs = model(inputs)
            outputs = torch.nn.functional.sigmoid(outputs)
            loss = criterion(outputs, labels)

            # backward
            loss.backward()
            optimizer.step()
            # 采用dice系数评价
            train_acc.update(metrics.dice_coeff(outputs, labels), outputs.size(0))
            train_loss.update(loss.data.item(), outputs.size(0))

            # tensorboard logging
            if step % hp.logging_step == 0:
                writer.log_training(train_loss.avg, train_acc.avg, step)
                loader.set_postfix(**{'lr': optimizer.param_groups[0]['lr'],
                                      'Loss': '{:.4f}'.format(train_loss.avg),
                                      'Acc': '{:.4f}'.format(train_acc.avg)})
                # wandb.log({'train_loss': '{:.4f}'.format(train_loss.avg),
                #            'train_acc': '{:.4f}'.format(train_acc.avg)})
                # Validatiuon
                if step % hp.validation_interval == 0:
                    # 关闭train进程的进度条
                    # loader.close()
                    valid_metrics = validation(val_dataloader, model, criterion, writer, step)
                    # 再打开train进程的进度条
                    # loader.update()
                    save_path = os.path.join(checkpoint_dir, "%s_checkpoint_%04d.pt" % (name, step))
                    # store best loss and save a model checkpoint
                    best_loss = min(valid_metrics["valid_loss"], best_loss)
                    torch.save(
                        {
                            "step": step,
                            "epoch": epoch,
                            "arch": "ResUnet",
                            "state_dict": model.state_dict(),
                            "best_loss": best_loss,
                            "optimizer": optimizer.state_dict(),
                        },
                        save_path,
                    )
                    # wandb.log(valid_metrics)
                    print("\nSaved checkpoint to: %s" % save_path)

            step += 1


def validation(valid_loader, model, criterion, logger, step):
    # logging accuracy and loss
    valid_acc = metrics.MetricTracker()
    valid_loss = metrics.MetricTracker()

    # switch to evaluate mode
    model.eval()

    # Iterate over data.
    loader = tqdm(valid_loader, desc="validation")
    for idx, data in enumerate(loader):

        # get the inputs and wrap in Variable
        inputs = data["sat_img"].cuda()
        labels = data["map_img"].cuda()

        # forward
        # prob_map = model(inputs) # last activation was a sigmoid
        # outputs = (prob_map > 0.3).float()
        outputs = model(inputs)
        outputs = torch.nn.functional.sigmoid(outputs)

        loss = criterion(outputs, labels)

        valid_acc.update(metrics.dice_coeff(outputs, labels), outputs.size(0))
        valid_loss.update(loss.data.item(), outputs.size(0))
        loader.set_postfix(**{'Loss': '{:.4f}'.format(valid_loss.avg),
                              'Acc': '{:.4f}'.format(valid_acc.avg)})
        if idx == 0:
            logger.log_images(inputs.cpu(), labels.cpu(), outputs.cpu(), step)
    logger.log_validation(valid_loss.avg, valid_acc.avg, step)
    # 打开model的训练模式
    model.train()
    return {"valid_loss": valid_loss.avg, "valid_acc": valid_acc.avg}


if __name__ == "__main__":
    # get命令行参数
    parser = argparse.ArgumentParser(description="Road and Building Extraction")
    # 数据集参数
    parser.add_argument("--epochs", default=5, type=int, metavar="N", help="number of total epochs to run")
    parser.add_argument("--resume", default="", type=str, metavar="PATH",
                        help="path to latest checkpoint (default: none)")
    parser.add_argument("--name", default="default", type=str, help="Experiment name")
    parser.add_argument("--separable_conv", action='store_true', default=True,
                        help="apply separable conv to decoder and aspp")
    parser.add_argument("--output_stride", type=int, default=16, choices=[8, 16])
    parser.add_argument("--num_classes", type=int, default=1,
                        help="num classes (default: None)")
    # 优化器参数
    parser.add_argument('--optimizer', type=str, default='Adam', help="the name of optimizer")
    # 其他参数
    parser.add_argument('--resume_train', type=str, default="", help="path of resume train model")
    args = parser.parse_args()

    # hp = HParam(args.config)
    hp = Config()

    main(hp, num_epochs=args.epochs, resume=args.resume, name=args.name)
