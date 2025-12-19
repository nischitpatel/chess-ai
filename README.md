# Chess AI Model API

This repository contains a **Chess AI model** trained on the [Lichess database](https://database.lichess.org/) for predicting optimal chess moves. The model is exposed as a **FastAPI backend**, which can be consumed by a frontend or any client to get AI-generated moves in real-time.

---

## Features

- Predicts the next best move for **white or black**.
- Supports multiple AI difficulty levels:
  - **Easy** → Random safe move
  - **Medium** → Minimax with limited depth
  - **Hard** → Minimax with advanced heuristics
  - **Grand-Master** → Deep neural network trained on Lichess data
- Accepts full **board state**, **turn**, and **move history**.
- Returns moves in a **simple JSON format**.
- Fully compatible with frontend chessboards for **real-time gameplay**.

---

## Tech Stack

- **Python** for AI model and backend
- **FastAPI** for REST API
- **Pandas / NumPy** for data processing
- **PyTorch** (or TensorFlow) for model training and inference
- **Lichess database** for training data
- **Uvicorn** for serving FastAPI app

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nischitpatel/chess-ai-model.git
cd chess-ai-model
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Usage

### Endpoint

**POST** `/predict-move`

**Request Body**:

```json
{
  "board": [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [null,null,null,null,null,null,null,null],
    [null,null,null,null,null,null,null,null],
    [null,null,null,null,null,null,null,null],
    [null,null,null,null,null,null,null,null],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
  ],
  "turn": "black",
  "history": []
}
```

* `board` → 8x8 array representing the current board state.

  * Uppercase letters → White pieces (`"P","R","N","B","Q","K"`)
  * Lowercase letters → Black pieces (`"p","r","n","b","q","k"`)
  * `null` → empty square
* `turn` → `"white"` or `"black"`.
* `history` → array of previous moves, where each move is an object:


**Response Body**:

```json
{
  "fromRow": 1,
  "fromCol": 4,
  "toRow": 3,
  "toCol": 4
}
```

* `fromRow` / `fromCol` → starting square of the move
* `toRow` / `toCol` → destination square of the move

> All coordinates are **0-indexed**.

---

## How the AI Works

1. **Input processing**:

   * Converts the 8x8 board array into **FEN notation**.
   * Considers move history for more accurate predictions.

2. **Difficulty levels**:

   * **Grand-Master** - Deep learning model trained on millions of Lichess games.

3. **Output**:

   * Returns the next move in JSON format.
   * Can be directly integrated into a frontend chessboard for real-time gameplay.

---

## Frontend Integration

Example usage with React:

```javascript
import { getAIMove } from "./utils/ai";

useEffect(() => {
  if (turn !== AI_COLOR) return;

  const makeAIMove = async () => {
    const aiMove = await getAIMove(board, AI_COLOR, history, aiLevel);
    if (!aiMove) return;

    setTimeout(() => {
      makeMove(aiMove.fromRow, aiMove.fromCol, aiMove.toRow, aiMove.toCol);
    }, 500);
  };

  makeAIMove();
}, [turn, board, aiLevel, history]);
```

---

## Example Python Client

```python
import requests

url = "http://127.0.0.1:8000/predict-move"
payload = {
    "board": [
        ["r","n","b","q","k","b","n","r"],
        ["p","p","p","p","p","p","p","p"],
        [None]*8,
        [None]*8,
        [None]*8,
        [None]*8,
        ["P"]*8,
        ["R","N","B","Q","K","B","N","R"]
    ],
    "turn": "black",
    "history": [],
    "level": "grand-master"
}

response = requests.post(url, json=payload)
print(response.json())
```

---

## Training

* Model trained on **millions of Lichess games**.
* Preprocessing steps:

  * Convert board positions to numeric / tensor representation.
  * Encode legal moves and game history.
* Optimized for fast inference (~<250ms per move).

> Raw Lichess database is not included due to size and licensing. Download from [Lichess Database](https://database.lichess.org/).

---

## Future Improvements

* Multi-step search (lookahead) using **Monte Carlo Tree Search**.
* Model compression for faster server inference.
* WebSocket integration for real-time multiplayer games.
* Multi-level AI for adaptive difficulty based on player skill.

---

## License

MIT License

---
