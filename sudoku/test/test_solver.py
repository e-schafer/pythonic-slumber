from re import S
import unittest

from sudoku.solver import Sudoku

solver = Sudoku(size=3)

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


class SolverTest(unittest.TestCase):
    """Test all subfunctions"""

    def test_col_possibilities(self):
        # check values for column 0
        self.assertCountEqual(solver.col_possibilities(grid1, 0), [1, 3, 7, 9])

    def test_row_possibilities(self):
        # check values for row 0
        self.assertCountEqual(solver.row_possibilities(grid1, 0), [1, 6])

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

        self.assertDictEqual(solver.sector_map(), expected)

    def test_sector_possibilities_1(self):
        # check values for the sector associated with the cell 0,0
        self.assertListEqual(solver.sector_possibilities(grid1, 0, 0), [1, 6, 7, 8, 9])

    def test_sector_possibilities_2(self):
        # check values for the sector associated with the cell 8,8
        self.assertListEqual(solver.sector_possibilities(grid1, 8, 8), [4, 7, 8])

    def test_sector_possibilities_3(self):
        # check values for the sector associated with the cell 0,8
        self.assertListEqual(
            solver.sector_possibilities(grid1, 0, 8), [1, 2, 3, 4, 8, 9]
        )


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(SolverTest())
