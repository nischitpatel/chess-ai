from fastapi import FastAPI
from pydantic import BaseModel
import torch
from model.policy_net import PolicyNet
from inference import select_best_move
from encode_move import decode_move
from encode_board import encode_board
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allows OPTIONS, POST, GET
    allow_headers=["*"],
)

# Load trained model
model = PolicyNet()
model.load_state_dict(torch.load("policy_net.pth"))
model.eval()

class BoardRequest(BaseModel):
    board: list  # 8x8 array of pieces as strings
    turn: str    # "white" or "black"
    # history: list = []

def board_to_fen(board, turn='b'):
    """
    board: 8x8 array, 'P', 'p', 'R', etc. or None
    turn: 'w' or 'b'
    """
    fen_rows = []
    for row in board:
        empty = 0
        fen_row = ''
        for cell in row:
            if cell is None:
                empty += 1
            else:
                if empty > 0:
                    fen_row += str(empty)
                    empty = 0
                fen_row += cell
        if empty > 0:
            fen_row += str(empty)
        fen_rows.append(fen_row)
    fen_board = '/'.join(fen_rows)
    # Basic FEN: board + turn + castling rights + en passant + halfmove + fullmove
    return f"{fen_board} {turn} KQkq - 0 1"


@app.post("/predict-move")
def predict_move(request: BoardRequest):
    # Convert board to tensor (8x8x12)
    board_tensor = encode_board(request.board) 
    board_tensor = torch.tensor(board_tensor, dtype=torch.float32)

    # Get best move ID from model
    board_fen = board_to_fen(request.board)
    move_id = select_best_move(model, board_tensor, board_fen)

    # Decode move ID - fromRow, fromCol, toRow, toCol
    from_row, from_col, to_row, to_col = decode_move(move_id)

    return {
        "fromRow": from_row,
        "fromCol": from_col,
        "toRow": to_row,
        "toCol": to_col
    }
