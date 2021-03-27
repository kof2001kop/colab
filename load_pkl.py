import torch
import torch.nn as nn

x = torch.tensor([[2., 3.]])

net = torch.load('colab/net.pkl')
result = net(x)

if (result[0][0] >= 0.5)
	print ("负")
else
	print ("正")

#print (result[0][0])
#print (result[0][1])