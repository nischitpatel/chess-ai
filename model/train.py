import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from policy_net import PolicyNet
from dataset import ChessDataset

def train_model(X, y, epochs=10, batch_size=64):
    dataset = ChessDataset(X, y)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = PolicyNet()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        total_loss = 0

        for boards, moves in loader:
            optimizer.zero_grad()
            logits = model(boards)
            loss = criterion(logits, moves)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}: Loss = {total_loss/len(loader):.4f}")

    torch.save(model.state_dict(), "policy_net.pth")
    return model
