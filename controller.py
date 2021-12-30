from view import TicTacToeView

from model import Grid

from enums import GameState

from analyzer import GameStateAnalyzer


class TicTacToeController:
    def __init__(
        self, grid: Grid,
        view: TicTacToeView,
    ):
        self.grid = grid
        self.view = view

    def run_game(self):
        self.print_grid()
        game_state = GameState.NOT_FINISHED

        while game_state == GameState.NOT_FINISHED:
            while True:
                try:
                    coordinates = self.view.show_coordinate_prompt()
                    valid_coordinates = self.grid.validate_coordinates(
                        coordinates
                    )
                    break
                except (ValueError, IndexError, TypeError) as error:
                    print(error)

            self.grid.update_grid(valid_coordinates)
            self.print_grid()

            self.grid.switch_player()
            analyser = GameStateAnalyzer(self.grid)
            game_state = analyser.analyze()
        else:
            self.view.show_message(game_state.value)

    def print_grid(self):
        printable_grid = self.grid.get_printable_grid()
        self.view.print_grid(printable_grid)
