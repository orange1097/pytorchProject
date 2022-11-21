import torch
import torch.nn as nn


def layer_norm_process(feature: torch.Tensor, beta=0., gamma=1., eps=1e-5):
    var_mean = torch.var_mean(feature, dim=-1, unbiased=False)
    # 均值
    mean = var_mean[1]
    # 方差
    var = var_mean[0]

    # layer norm process
    feature = (feature - mean[..., None]) / torch.sqrt(var[..., None] + eps)
    feature = feature * gamma + beta

    return feature


def main():
    t = torch.rand(4, 2, 3)
    print(t)
    # 仅在最后一个维度上做norm处理
    norm = nn.LayerNorm(normalized_shape=t.shape[-1], eps=1e-5)# LN传入的是对应维度的形状。BN传入的参数是Channel数
    # 官方layer norm处理
    t1 = norm(t)
    # 自己实现的layer norm处理
    t2 = layer_norm_process(t, eps=1e-5)
    print("t1:\n", t1)
    print("t2:\n", t2)


if __name__ == '__main__':
    main()

