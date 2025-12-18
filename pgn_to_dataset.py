import chess
import chess.pgn
import numpy as np

from encode_board import encode_board
from encode_move import encode_move

def board_to_array(board):
    arr = [[None]*8 for _ in range(8)]
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - (square // 8)
            col = square % 8
            arr[row][col] = piece.symbol()
    return arr

def build_dataset(pgn_path, max_games=1000):
    X = []
    y = []

    with open(pgn_path) as pgn:
        for _ in range(max_games):
            game = chess.pgn.read_game(pgn)
            if game is None:
                break

            board = game.board()

            for move in game.mainline_moves():
                board_array = board_to_array(board)
                X.append(encode_board(board_array))

                from_sq = move.from_square
                to_sq = move.to_square

                from_row = 7 - (from_sq // 8)
                from_col = from_sq % 8
                to_row = 7 - (to_sq // 8)
                to_col = to_sq % 8

                y.append(encode_move(from_row, from_col, to_row, to_col))

                board.push(move)

    return np.array(X), np.array(y)

X, y = build_dataset("sample.pgn", max_games=5)

print(X.shape)  # (num_moves, 8, 8, 12)
print(y.shape)  # (num_moves,)
