import itertools
from typing import List

from enums import FieldState


class Grid:
    GRID_SIZE = 3

    @classmethod
    def from_string(cls, field_states: str) -> 'Grid':
        parsed_grid = [FieldState(field_state) for field_state in field_states]
        nested_grid = [parsed_grid[index:index + cls.GRID_SIZE]
                       for index in range(0, len(parsed_grid), cls.GRID_SIZE)]

        return cls(nested_grid)

    def __init__(self, initial_state: List[List[FieldState]]):
        self._grid = initial_state
        self.current_player = FieldState.X

    def __iter__(self):
        return self._grid.__iter__()

    def __getitem__(self, item):
        return self._grid.__getitem__(item)

    def get_grid(self):
        return self._grid

    def get_printable_grid(self) -> List[List[str]]:
        printable_grid = []

        for row in self._grid:
            printable_grid.append(
                list(
                    map(
                        lambda field: field.value,
                        row
                    )
                )
            )

        return printable_grid

    @classmethod
    def generate_empty_grid(cls) -> List[List[FieldState]]:
        empty_grid = []

        for _ in range(0, cls.GRID_SIZE):
            row = [FieldState.EMPTY for _ in range(0, cls.GRID_SIZE)]
            empty_grid.append(row)

        return empty_grid

    def get_transposed_grid(self) -> List[List[FieldState]]:
        # python does not support predefining the size of a list,
        # hence we use a prepopulated empty grid instead
        transposed_grid = self.generate_empty_grid()

        for row_index, row in enumerate(self._grid):
            for column_index, field in enumerate(row):
                transposed_grid[column_index][row_index] = field

        return transposed_grid

    def as_flat_list(self) -> List[FieldState]:
        return [field for field in itertools.chain(*self._grid)]

    @staticmethod
    def _are_coordinates_numeric(coordinates: List[str]):
        for coordinate in coordinates:
            if not coordinate.isnumeric():
                raise TypeError("You should enter numbers!")

    @classmethod
    def _are_coordinates_on_grid(cls, coordinates: List[int]):
        upper_coordinate_limit = cls.GRID_SIZE + 1
        allowed_coordinate_range = range(1, upper_coordinate_limit)

        for coordinate in coordinates:
            if coordinate not in allowed_coordinate_range:
                raise IndexError(
                    f"Coordinates should be from 1 to {cls.GRID_SIZE}!"
                )

    @staticmethod
    def _translate_coordinates(coordinates: List[int]):
        return [coordinate - 1 for coordinate in coordinates]

    @staticmethod
    def _parse_str_coordinates(coordinates_list: List[str]) -> List[int]:
        return list(
            map(
                lambda coordinate: int(coordinate),
                coordinates_list
            )
        )

    def _is_field_occupied(self, coordinates: List[int]):
        field_state = self._grid[coordinates[0]][coordinates[1]]

        if field_state != FieldState.EMPTY:
            raise ValueError("This cell is occupied! Choose another one!")

    def validate_coordinates(self, coordinates: str) -> List[int]:
        coordinates_list = coordinates.split()
        self._are_coordinates_numeric(
            coordinates_list
        )

        parsed_coordinates = self._parse_str_coordinates(coordinates_list)
        self._are_coordinates_on_grid(
            parsed_coordinates
        )

        translated_coordinates = self._translate_coordinates(
            parsed_coordinates
        )
        self._is_field_occupied(translated_coordinates)

        return translated_coordinates

    def update_grid(self, coordinates: List[int]):
        self._grid[coordinates[0]][coordinates[1]] = self.current_player

    def switch_player(self):
        self.current_player = FieldState.O if \
            self.current_player == FieldState.X else FieldState.X
