import torch
import torch.nn as nn

x1_t = torch.randn(10);
x2_t = torch.randn(10);

#y_t = 2 * x1_t + x2_t

print (x1_t)
print (x2_t)
print (torch.stack([x1_t, x2_t],dim=1))

