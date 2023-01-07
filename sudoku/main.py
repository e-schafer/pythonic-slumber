from pprint import pprint

from solver import Sudoku
from copy import deepcopy

grid1 = [
    [1, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 6, 0, 2, 0, 7, 0, 0],
    [7, 8, 9, 4, 5, 0, 1, 0, 3],
    [0, 0, 0, 8, 0, 7, 0, 0, 4],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 4, 2, 0, 1],
    [3, 1, 2, 9, 7, 0, 0, 4, 0],
    [0, 4, 0, 0, 1, 2, 0, 7, 8],
    [9, 0, 8, 0, 0, 0, 0, 0, 0],
]

grid2 = [
    [3, 0, 0, 8, 0, 1, 0, 0, 2],
    [2, 0, 1, 0, 3, 0, 6, 0, 4],
    [0, 0, 0, 2, 0, 4, 0, 0, 0],
    [8, 0, 9, 0, 0, 0, 1, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 5, 0],
    [7, 0, 2, 0, 0, 0, 4, 0, 9],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [9, 0, 4, 0, 8, 0, 7, 0, 5],
    [6, 0, 0, 1, 0, 7, 0, 0, 3],
]

if __name__ == "__main__":
    sudoku = Sudoku(size=3)
    print("GRID 1")
    pprint(grid1)
    sudoku.solve_grid(deepcopy(grid1), 0, 0)
    print("---------------------------------")
    pprint(sudoku.result_grid)
    print("================================")
    print("GRID 2")
    pprint(grid2)
    sudoku.solve_grid(deepcopy(grid2), 0, 0)
    print("---------------------------------")
    pprint(sudoku.result_grid)
