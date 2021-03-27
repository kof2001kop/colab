import torch
import torch.nn as nn

x1_t = torch.randn(10);
x2_t = torch.randn(10);
x_t = torch.stack([x1_t, x2_t],dim=1)

y_t = x1_t * x2_t

print (x1_t)
print (x2_t)
print (y_t)

