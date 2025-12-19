import torch
from model.policy_net import PolicyNet

model = PolicyNet()
model.load_state_dict(torch.load("policy_net.pth"))
model.eval()

# Pick random board from dataset
board_tensor = X[0].permute(2,0,1).unsqueeze(0)  # (1,12,8,8)
logits = model(board_tensor)
print("Predicted move logits:", logits.shape)
