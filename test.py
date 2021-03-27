import torch
import torch.nn as nn

x1_t = torch.randn(10);
x2_t = torch.randn(10);
x_input = torch.stack([x1_t, x2_t],dim=1)

y_t = x1_t * x2_t
zero = torch.zeros_like(y_t)
one = torch.ones_like(y_t)

left = torch.where(y_t > 0, one, zero)
right = torch.where(y_t > 0, zero, one)
y_out = torch.stack([left, right],dim=1)

print (left)
print (right)
print (y_out)
