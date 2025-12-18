import torch
import numpy as np
from legal_moves import get_legal_move_ids

def select_best_move(model, board_tensor, board_fen):
    model.eval()

    with torch.no_grad():
        logits = model(board_tensor.unsqueeze(0))[0]  # (4096,)

    legal_move_ids = get_legal_move_ids(board_fen)

    mask = torch.full((4096,), float("-inf"))
    mask[legal_move_ids] = 0

    masked_logits = logits + mask
    best_move_id = torch.argmax(masked_logits).item()

    return best_move_id

from encode_move import decode_move

move_id = select_best_move(...)
from_row, from_col, to_row, to_col = decode_move(move_id)
