from policy_net import PolicyNet
import torch

model = PolicyNet()
x = torch.randn(2, 12, 8, 8)

out = model(x)
print(out.shape)
