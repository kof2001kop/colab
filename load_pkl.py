import torch
import torch.nn as nn

x = torch.tensor([[2., 3.]])

net = torch.load('colab/net.pkl')
result = net(x)

print (result)