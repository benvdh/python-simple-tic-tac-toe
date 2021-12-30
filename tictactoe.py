from view import TicTacToeView
from model import Grid
from controller import TicTacToeController

empty_grid_state = Grid.generate_empty_grid()

grid = Grid(empty_grid_state)
view = TicTacToeView()
controller = TicTacToeController(grid, view)

controller.run_game()
