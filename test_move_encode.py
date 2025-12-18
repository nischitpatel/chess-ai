from encode_move import encode_move, decode_move

move_id = encode_move(6, 4, 4, 4)  # e2 → e4
decoded = decode_move(move_id)

assert decoded == (6, 4, 4, 4)
print("Move encoding works")
