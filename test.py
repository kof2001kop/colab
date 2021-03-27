import torch
import torch.nn as nn
'''
x1_t = torch.randn(10);
x2_t = torch.randn(10);
x_input = torch.stack([x1_t, x2_t],dim=1)

y_t = x1_t * x2_t
zero = torch.zeros_like(y_t)
one = torch.ones_like(y_t)

left = torch.where(y_t > 0, one, zero)
right = torch.where(y_t > 0, zero, one)
y_tag = torch.stack([left, right],dim=1)
'''
x1_t = torch.normal(2*torch.ones(5,2),1)
y1_t = torch.zeros(5)

x2_t = torch.normal(-2*torch.ones(5,2),1)
y2_t = torch.ones(5)

x_t = torch.cat((x1_t,x2_t),0)
y_t = torch.cat((y1_t,y2_t),0)

print (x_t)
print (y_t)