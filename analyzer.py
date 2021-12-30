from typing import List, Optional

from model import Grid
from enums import FieldState, GameState


class GameStateAnalyzer:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.winning_rows = self._detect_winning_rows(self.grid.get_grid())
        self.winning_columns = self._detect_winning_rows(
            self.grid.get_transposed_grid()
        )
        self.winning_diagonals = self._detect_winning_diagonals()

    @staticmethod
    def _detect_winning_rows(
        grid: List[List[FieldState]]
    ) -> List[List[FieldState]]:
        winning_rows = []

        for row in grid:
            unique_values = set(row)
            no_empty_fields = FieldState.EMPTY not in unique_values

            if len(unique_values) == 1 and no_empty_fields:
                winning_rows.append(row)

        return winning_rows

    def _detect_winning_diagonals(self) -> List[List[FieldState]]:
        forward_diagonal = []
        backward_diagonal = []
        winning_diagonals = []
        double_iterator = zip(
            range(0, Grid.GRID_SIZE),
            range(Grid.GRID_SIZE - 1, -1, -1)
        )

        for row_index, column_index in double_iterator:
            forward_diagonal.append(self.grid[row_index][row_index])
            backward_diagonal.append(self.grid[row_index][column_index])

        for diagonal in [forward_diagonal, backward_diagonal]:
            unique_values = set(diagonal)
            no_empty_fields = FieldState.EMPTY not in unique_values

            if len(unique_values) == 1 and no_empty_fields:
                winning_diagonals.append(list(diagonal))

        return winning_diagonals

    def get_count_by_field_state(self, field_state: FieldState) -> int:
        flat_grid = self.grid.as_flat_list()

        return flat_grid.count(field_state)

    def has_empty_cells(self):
        return self.get_count_by_field_state(FieldState.EMPTY) > 0

    def has_no_winners(self):
        return not self.winning_rows and not self.winning_columns and \
               not self.winning_diagonals

    def is_game_in_progress(self):
        return self.has_empty_cells() and self.has_no_winners()

    def is_draw(self):
        return not self.has_empty_cells() and self.has_no_winners()

    def has_impossible_state(self):
        x_count = self.get_count_by_field_state(FieldState.X)
        o_count = self.get_count_by_field_state(FieldState.O)

        difference = x_count - o_count \
            if x_count > o_count else o_count - x_count

        return difference >= 2 or \
            len(self.winning_rows) > 1 or \
            len(self.winning_columns) > 1 or \
            len(self.winning_diagonals) > 1

    @staticmethod
    def detect_winner(
        winner_state: List[List[FieldState]]
    ) -> Optional[GameState]:
        if winner_state:
            field_state = winner_state[0][0]
            winner = GameState.X_WINS if field_state == FieldState.X \
                else GameState.O_WINS
            return winner
        else:
            return None

    def analyze(self) -> Optional[GameState]:
        has_impossible_state = self.has_impossible_state()
        if self.is_game_in_progress() and not has_impossible_state:
            return GameState.NOT_FINISHED

        if has_impossible_state:
            return GameState.IMPOSSIBLE

        if self.is_draw():
            return GameState.DRAW

        winner_states = [
            self.winning_rows,
            self.winning_columns,
            self.winning_diagonals
        ]

        for winner_state in winner_states:
            winner = self.detect_winner(winner_state)

            if winner is not None:
                return winner

        return None
