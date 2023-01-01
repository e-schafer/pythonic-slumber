import functools
import itertools

UNDECLARED_CELL = -1


class Sudoku:
    def __init__(self, grille: list[list[int]], size: int):
        self.grille = grille
        self.size = size

    @functools.lru_cache
    def possible_values(self):
        return range(1, self.size**2 + 1)

    def col_possibilities(self, x: int):
        return [
            self.grille[i][x]
            for i in range(0, self.size**2)
            if self.grille[i][x] > UNDECLARED_CELL
        ]

    def row_possibilities(self, y: int) -> list[int]:
        return list(filter(lambda x: x != UNDECLARED_CELL, self.grille[y]))

    def solve_grille(self):
        pass
