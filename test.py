import torch
import torch.nn as nn

net = nn.Sequential(
    nn.Linear(2,5),  # 输入层与第一隐层结点数设置，全连接结构
    nn.Sigmoid(),  # 第一隐层激活函数采用sigmoid
    nn.Linear(5,5),  # 第一隐层与第二隐层结点数设置，全连接结构
    nn.Sigmoid(),  # 第一隐层激活函数采用sigmoid
    nn.Linear(5,2),  # 第二隐层与输出层层结点数设置，全连接结构
    nn.Softmax(dim=1) # 由于有两个概率输出，因此对其使用Softmax进行概率归一化，dim=1代表行归一化
)

# 配置损失函数和优化器
optimizer = torch.optim.SGD(net.parameters(),lr=0.01) # 优化器使用随机梯度下降，传入网络参数和学习率
loss_func = torch.nn.CrossEntropyLoss() # 损失函数使用交叉熵损失函数

