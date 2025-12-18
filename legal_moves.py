import chess
from encode_move import encode_move

def get_legal_move_ids(board_fen):
    board = chess.Board(board_fen)
    legal_ids = []

    for move in board.legal_moves:
        from_sq = move.from_square
        to_sq = move.to_square

        from_row = 7 - (from_sq // 8)
        from_col = from_sq % 8
        to_row = 7 - (to_sq // 8)
        to_col = to_sq % 8

        legal_ids.append(
            encode_move(from_row, from_col, to_row, to_col)
        )

    return legal_ids
