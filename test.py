import torch
import torch.nn as nn

#x1_t = torch.randn(10);
#x2_t = torch.randn(10);

#y_t = 2 * x1_t + x2_t

x1_t = torch.normal(2*torch.ones(10,2),1)
y1_t = torch.zeros(10)

x2_t = torch.normal(-2*torch.ones(10,2),1)
y2_t = torch.ones(10)

x_t = torch.cat((x1_t,x2_t),0)

print (x1_t)
print (x2_t)
print (xt_t)

