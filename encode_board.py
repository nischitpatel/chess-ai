import numpy as np

PIECE_TO_CHANNEL = {
    "P": 0, "N": 1, "B": 2, "R": 3, "Q": 4, "K": 5,
    "p": 6, "n": 7, "b": 8, "r": 9, "q": 10, "k": 11
}

def encode_board(board):
    """
    board: 8x8 list (same format as frontend)
    returns: numpy array (8, 8, 12)
    """
    tensor = np.zeros((8, 8, 12), dtype=np.float32)

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is None:
                continue

            channel = PIECE_TO_CHANNEL.get(piece)
            if channel is not None:
                tensor[row, col, channel] = 1.0

    return tensor
