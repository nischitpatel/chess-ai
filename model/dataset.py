import torch
from torch.utils.data import Dataset

class ChessDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        board = self.X[idx].permute(2, 0, 1)  # (12, 8, 8)
        move = self.y[idx]
        return board, move
