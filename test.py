import torch.nn.*

net = nn.Sequential(
    nn.Linear(2,5),  # 输入层与第一隐层结点数设置，全连接结构
    torch.nn.Sigmoid(),  # 第一隐层激活函数采用sigmoid
    nn.Linear(5,5),  # 第一隐层与第二隐层结点数设置，全连接结构
    torch.nn.Sigmoid(),  # 第一隐层激活函数采用sigmoid
    nn.Linear(5,2),  # 第二隐层与输出层层结点数设置，全连接结构
    nn.Softmax(dim=1) # 由于有两个概率输出，因此对其使用Softmax进行概率归一化，dim=1代表行归一化
)

print(net)

