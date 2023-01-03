from collections import deque
import functools
import itertools
from pprint import pprint

UNDECLARED_CELL = 0


class Sudoku:
    def __init__(self, size: int):
        self.size = size
        self.grille: list[list[int]]

    @functools.lru_cache
    def possible_values(self):
        return set(range(1, self.size**2 + 1))

    @functools.lru_cache
    def sector_map(self) -> dict[int, list[tuple[int, int]]]:
        sector_dict: dict[int, list[tuple[int, int]]] = {}
        for i in range(0, self.size**2):
            sector_dict[i] = list()
            offset_Y, offset_X = divmod(i, 3)
            for x in range(offset_X * self.size, offset_X * self.size + self.size):
                for y in range(offset_Y * self.size, offset_Y * self.size + self.size):
                    sector_dict[i].append((x, y))
        return sector_dict

    @functools.lru_cache
    def reverse_sector_map(self) -> dict[tuple[int, int], list[tuple[int, int]]]:
        dict_coord = {}
        for key, value in self.sector_map().items():
            for coord in value:
                dict_coord[coord] = value
        return dict_coord

    def col_possibilities(self, grille, x: int) -> list[int]:
        return sorted(
            filter(
                lambda x: x > UNDECLARED_CELL,
                map(lambda i: grille[i][x], range(0, self.size**2)),
            )
        )

    def row_possibilities(self, grille: list[list[int]], y: int) -> list[int]:
        return list(sorted(filter(lambda x: x != UNDECLARED_CELL, grille[y])))

    def sector_possibilities(
        self, grille: list[list[int]], coord_x: int, coord_y: int
    ) -> list[int]:
        return list(
            sorted(
                filter(
                    lambda x: x > UNDECLARED_CELL,
                    map(
                        # x and y are flipped when accessing the initial grid du to the list of list
                        lambda x: grille[x[1]][x[0]],
                        self.reverse_sector_map()[(coord_x, coord_y)],
                    ),
                )
            )
        )

    def is_valid(self, grille: list[list[int]], x: int, y: int, val_to_check: int):
        used_p: set[int] = set(
            itertools.chain(
                self.row_possibilities(grille, y),
                self.col_possibilities(grille, x),
                self.sector_possibilities(grille, x, y),
            )
        )
        return val_to_check not in used_p

    def solve_grille(self, grille: list[list[int]], x: int = 0, y: int = 0) -> bool:
        """ """
        self.grille = grille
        next_y, next_x = divmod((x + 1) + (y * self.size**2), self.size**2)
        if x > 8 or y > 8:
            # print(f"exit end of grid, x={x}, y={y}")
            return True
        if grille[y][x] == 0:
            for val in range(1, self.size**2 + 1):
                if self.is_valid(grille, x, y, val):
                    # print(f"Try -- val={val}, x={x}, y={y}")
                    grille[y][x] = val
                    if self.solve_grille(grille, next_x, next_y):
                        # print(f"Validate -- val={val}, x={x}, y={y}")
                        return True
                    grille[y][x] = 0
        else:
            # print(f"Skip cell -- x={x}, y={y}")
            if self.solve_grille(grille, next_x, next_y):
                return True
        # print(f"End function -- x={x}, y={y}")
        return False
