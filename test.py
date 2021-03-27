import torch
import torch.nn as nn

#x1_t = torch.randn(10);
#x2_t = torch.randn(10);

#y_t = 2 * x1_t + x2_t

x1_t = torch.normal(2*torch.ones(100,2),1)
y1_t = torch.zeros(100)

print (y1_t)
