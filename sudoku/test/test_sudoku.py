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

    def test_sector_map(self):
        expected: dict[int, list[tuple[int, int]]] = {
            0: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
            1: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
            2: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
            3: [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
            4: [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
            5: [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
            6: [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
            7: [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
            8: [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
        }

        self.assertDictEqual(test_sudoku.sector_map(), expected)

    def test_sector_possibilities_1(self):
        self.assertListEqual(test_sudoku.sector_possibilities(0, 0), [1, 7, 8, 6, 9])

    def test_sector_possibilities_2(self):
        self.assertListEqual(test_sudoku.sector_possibilities(8, 8), [4, 7, 8])

    def test_sector_possibilities_3(self):
        self.assertListEqual(test_sudoku.sector_possibilities(0, 8), [3, 9, 1, 4, 2, 8])


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(SudokuTest())
