import torch
import torch.nn as nn

x1_t = torch.randn(10);
x2_t = torch.randn(10);

m = 2 * x1_t
y_t = m + x2_t

print (m)
print (x2_t)
print (y_t)
