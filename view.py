from typing import List


class TicTacToeView:
    CELLS_PROMPT = "Enter cells: "
    HORIZONTAL_BOUNDARY = "---------"
    COORDINATES_PROMPT = "Enter the coordinates: "

    @classmethod
    def show_cells_prompt(cls):
        return input(cls.CELLS_PROMPT)

    @classmethod
    def _print_horizontal_boundary(cls):
        print(cls.HORIZONTAL_BOUNDARY)

    @classmethod
    def print_grid(cls, grid: List[List[str]]):
        cls._print_horizontal_boundary()

        for row in grid:
            print(f"| {' '.join(row)} |")

        cls._print_horizontal_boundary()

    @staticmethod
    def show_message(message: str):
        print(message)

    @classmethod
    def show_coordinate_prompt(cls):
        return input(cls.COORDINATES_PROMPT)
