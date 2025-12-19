from pgn_to_dataset import build_dataset
from model.train import train_model

# Build dataset (example)
X, y = build_dataset("data/lichess_db_standard_rated_2014-01.pgn", max_games=5000)
model = train_model(X, y, epochs=5)
