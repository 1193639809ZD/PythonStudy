import torch
from torch import nn
from torch.nn import functional as f
import argparse
import os
from eveLeaf.utils import TrainUtils as Utils


def main():
    # 加载模型
    model = args.model_name
    # 加载优化器
    optimizer = Utils.get_optimizer(model, args)
    # 判断是否恢复训练
    if args.resume_train:
        if os.path.isfile(args.resume_train):
            print("=> loading checkpoint '{}'".format(args.resume_train))
            checkpoint = torch.load(args.resume_train)

            start_epoch = checkpoint["epoch"]

            best_loss = checkpoint["best_loss"]
            model.load_state_dict(checkpoint["state_dict"])
            optimizer.load_state_dict(checkpoint["optimizer"])
            print(
                "=> loaded checkpoint '{}' (epoch {})".format(
                    args.resume_train, checkpoint["epoch"]
                )
            )
        else:
            print("=> no checkpoint found at '{}'".format(args.resume))


if __name__ == '__main__':
    # get命令行参数
    parser = argparse.ArgumentParser(description='Pytorch Train Template')
    # 数据集参数
    parser.add_argument('--batch_size', default=16)
    # 优化器参数
    parser.add_argument('--optimizer', type=str, default='Adam', help="the name of optimizer")
    # 模型参数
    parser.add_argument('--model_name', type=str, default='ResUnet', help="the name of model")
    # 其他参数
    parser.add_argument('--resume_train', type=str, default="", help="path of resume train model")
    args = parser.parse_args()
