import torch
import torch.nn as nn

net = nn.Sequential(
    nn.Linear(2,5),  
    torch.nn.Sigmoid(),  
    nn.Linear(5,5),  
    torch.nn.Sigmoid(),  
    nn.Linear(5,2),  
    nn.Softmax(dim=1) )

torch.load('colab/net.pkl')
#net.load_state_dict(torch.load('colab/net.pkl'))