import enum


class FieldState(enum.Enum):
    EMPTY = "_"
    X = "X"
    O = "O"


class GameState(enum.Enum):
    NOT_FINISHED = "Game not finished"
    DRAW = "Draw"
    X_WINS = "X wins"
    O_WINS = "O wins"
    IMPOSSIBLE = "Impossible"
