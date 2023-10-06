# timm的基本使用
import timm
import torch

if __name__ == '__main__':
    print("如果不设置num_classes，表示使用的是原始的预训练模型的分类层")
    m = timm.create_model('resnet50', pretrained=True)
    m.eval()
    o = m(torch.randn(2, 3, 224, 224))
    print(f'Classification layer shape: {o.shape}')
    # 输出flatten层或者global_pool层的前一层的数据（flatten层和global_pool层通常接分类层）
    o = m.forward_features(torch.randn(2, 3, 224, 224))
    print(f'Feature shape: {o.shape}\n')
