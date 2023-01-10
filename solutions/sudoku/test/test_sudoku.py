import unittest

from sudoku.solver import Sudoku


solver: Sudoku = Sudoku(size=3)


class SudokuTest(unittest.TestCase):
    """Solve 2 grids just to be sure =D"""

    def test_solve_grid1(self):
        grid = [
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

        grid_soluce = [
            [1, 2, 3, 7, 8, 9, 4, 5, 6],
            [4, 5, 6, 1, 2, 3, 7, 8, 9],
            [7, 8, 9, 4, 5, 6, 1, 2, 3],
            [2, 3, 1, 8, 9, 7, 5, 6, 4],
            [5, 6, 4, 2, 3, 1, 8, 9, 7],
            [8, 9, 7, 5, 6, 4, 2, 3, 1],
            [3, 1, 2, 9, 7, 8, 6, 4, 5],
            [6, 4, 5, 3, 1, 2, 9, 7, 8],
            [9, 7, 8, 6, 4, 5, 3, 1, 2],
        ]

        solver.solve_grid(grid, 0, 0)
        for index in range(
            0,
            len(grid_soluce),
        ):
            self.assertListEqual(solver.result_grid[index], grid_soluce[index])

    def test_solve_grid2(self):
        grid = [
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

        grid_soluce = [
            [3, 4, 6, 8, 9, 1, 5, 7, 2],
            [2, 9, 1, 7, 3, 5, 6, 8, 4],
            [5, 7, 8, 2, 6, 4, 3, 9, 1],
            [8, 5, 9, 4, 7, 3, 1, 2, 6],
            [4, 6, 3, 9, 1, 2, 8, 5, 7],
            [7, 1, 2, 6, 5, 8, 4, 3, 9],
            [1, 3, 7, 5, 4, 9, 2, 6, 8],
            [9, 2, 4, 3, 8, 6, 7, 1, 5],
            [6, 8, 5, 1, 2, 7, 9, 4, 3],
        ]

        solver.solve_grid(grid, 0, 0)
        for index in range(
            0,
            len(grid_soluce),
        ):
            self.assertListEqual(solver.result_grid[index], grid_soluce[index])


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(SudokuTest())
