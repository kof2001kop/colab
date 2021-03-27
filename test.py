import torch
import torch.nn as nn

x1_t = (10 * torch.randn(10000)).ceil();
x2_t = (10 * torch.randn(10000)).ceil();
x_input = torch.stack([x1_t, x2_t],dim=1)

y_t = x1_t * x2_t
zero = torch.zeros_like(y_t)
one = torch.ones_like(y_t)

y_tag = torch.where(y_t > 0, one, zero)

#print (x_input)
#print (y_tag)

'''
x1_t = torch.normal(2*torch.ones(10,2),1)
y1_t = torch.zeros(10)

x2_t = torch.normal(-2*torch.ones(10,2),1)
y2_t = torch.ones(10)

x_input = torch.cat((x1_t,x2_t),0)
y_tag = torch.cat((y1_t,y2_t),0)
'''


net = nn.Sequential(
    nn.Linear(2,3),  # 输入层与第一隐层结点数设置，全连接结构
    torch.nn.Sigmoid(),  # 第一隐层激活函数采用sigmoid
    nn.Linear(3,2),  # 第二隐层与输出层层结点数设置，全连接结构
    nn.Softmax(dim=1) # 由于有两个概率输出，因此对其使用Softmax进行概率归一化
)


# 配置损失函数和优化器
optimizer = torch.optim.SGD(net.parameters(),lr=0.01) # 优化器使用随机梯度下降，传入网络参数和学习率
loss_func = torch.nn.CrossEntropyLoss() # 损失函数使用交叉熵损失函数


# 模型训练
num_epoch = 10000 # 最大迭代更新次数
for epoch in range(num_epoch):
    y_p = net(x_input)  # 喂数据并前向传播

    loss = loss_func(y_p,y_tag.long()) # 计算损失
    
    #PyTorch默认会对梯度进行累加，因此为了不使得之前计算的梯度影响到当前计算，需要手动清除梯度。
    #pyTorch这样子设置也有许多好处，但是由于个人能力，还没完全弄懂。
    
    optimizer.zero_grad()  # 清除梯度
    loss.backward()  # 计算梯度，误差回传
    optimizer.step()  # 根据计算的梯度，更新网络中的参数

    if epoch % 1000 == 0:
        print('epoch: {}, loss: {}'.format(epoch, loss.data.item()))

torch.save(net,'colab/net.pkl')
