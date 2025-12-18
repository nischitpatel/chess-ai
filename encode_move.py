def encode_move(from_row, from_col, to_row, to_col):
    from_sq = from_row * 8 + from_col
    to_sq = to_row * 8 + to_col
    return from_sq * 64 + to_sq


def decode_move(move_id):
    from_sq = move_id // 64
    to_sq = move_id % 64

    return (
        from_sq // 8,
        from_sq % 8,
        to_sq // 8,
        to_sq % 8
    )
