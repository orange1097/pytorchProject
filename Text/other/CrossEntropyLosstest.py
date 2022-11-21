import torch.nn as nn
import torch

x = torch.rand((3,3))
print(x)
y = torch.tensor([0, 1, 1])

softmax = nn.Softmax(dim=1)
x_softmax = softmax(x)
print(x_softmax)

x_log = torch.log(x_softmax)
print(x_log)
# ls = nn.LogSoftmax(dim=1)
# ls(x)

print("----------------------------")
print(range(len(x)))
loss = x_log[range(len(x)), y]  #取出每一个样本标签值处的概率
print(loss)
loss = abs(sum(loss)/len(x)) # 求平均损失
# #loss
# >>>tensor(1.0646)

