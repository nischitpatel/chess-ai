from encode_board import encode_board

test_board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [None]*8,
    [None]*8,
    [None]*8,
    [None]*8,
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"],
]

tensor = encode_board(test_board)

# White king
assert tensor[7][4][5] == 1

# Black queen
assert tensor[0][3][10] == 1

# Empty square
assert tensor[4][4].sum() == 0

print("Board encoding works perfectly")
