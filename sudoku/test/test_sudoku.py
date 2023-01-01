import unittest

from sudoku.solver import Sudoku

test_grille1 = [
    [1, -1, -1, -1, -1, -1, -1, -1, 6],
    [-1, -1, 6, -1, 2, -1, 7, -1, -1],
    [7, 8, 9, 4, 5, -1, 1, -1, 3],
    [-1, -1, -1, 8, -1, 7, -1, -1, 4],
    [-1, -1, -1, -1, 3, -1, -1, -1, -1],
    [-1, 9, -1, -1, -1, 4, 2, -1, 1],
    [3, 1, 2, 9, 7, -1, -1, 4, -1],
    [-1, 4, -1, -1, 1, 2, -1, 7, 8],
    [9, -1, 8, -1, -1, -1, -1, -1, -1],
]

test_sudoku = Sudoku(test_grille1, 3)


class SudokuTest(unittest.TestCase):
    def test_col_possibilities(self):
        self.assertListEqual(test_sudoku.col_possibilities(0), [1, 7, 3, 9])

    def test_row_possibilities(self):
        self.assertListEqual(test_sudoku.row_possibilities(0), [1, 6])


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(SudokuTest())
