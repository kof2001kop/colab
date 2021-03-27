import torch
import torch.nn as nn

x1_t = torch.randn(10);
x2_t = torch.randn(10);
x_input = torch.stack([x1_t, x2_t],dim=1)

y_t = x1_t * x2_t
zero = torch.zeros_like(y_t)
one = torch.ones_like(y_t)

y_tag = torch.where(y_t > 0, one, zero)

print (x_input)
print (y_tag)