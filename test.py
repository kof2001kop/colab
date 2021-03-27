import torch
import torch.nn as nn

x_t = torch.empty(10).range(100);
print(x_t)

'''
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

num_epoch = 10000 # 最大迭代更新次数
for epoch in range(num_epoch):
    y_p = net(x_t)  # 喂数据并前向传播

    loss = loss_func(y_p,y_t.long()) # 计算损失
    '''
    PyTorch默认会对梯度进行累加，因此为了不使得之前计算的梯度影响到当前计算，需要手动清除梯度。
    pyTorch这样子设置也有许多好处，但是由于个人能力，还没完全弄懂。
    '''
    optimizer.zero_grad()  # 清除梯度
    loss.backward()  # 计算梯度，误差回传
    optimizer.step()  # 根据计算的梯度，更新网络中的参数

    #if epoch % 1000 == 0:
    #    print('epoch: {}, loss: {}'.format(epoch, loss.data.item()))
        
'''