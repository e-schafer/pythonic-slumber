import functools
import itertools
from pprint import pprint

UNDECLARED_CELL = 0


class Sudoku:
    def __init__(self, grille: list[list[int]], size: int):
        self.grille = grille
        self.size = size

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

    def col_possibilities(self, x: int) -> list[int]:
        return sorted(
            [
                self.grille[i][x]
                for i in range(0, self.size**2)
                if self.grille[i][x] > UNDECLARED_CELL
            ]
        )

    def row_possibilities(self, y: int) -> list[int]:
        return list(sorted(filter(lambda x: x != UNDECLARED_CELL, self.grille[y])))

    def sector_possibilities(self, coord_x: int, coord_y: int) -> list[int]:
        return list(
            sorted(
                filter(
                    lambda x: x > UNDECLARED_CELL,
                    map(
                        # x and y are flipped when accessing the initial grid du to the list of list
                        lambda x: self.grille[x[1]][x[0]],
                        self.reverse_sector_map()[(coord_x, coord_y)],
                    ),
                )
            )
        )

    def solve_grille(self):
        for y in range(0, self.size**2):
            for x in range(0, self.size**2):
                if self.grille[y][x] == 0:
                    r_p = self.row_possibilities(y)
                    c_p = self.col_possibilities(x)
                    s_p = self.sector_possibilities(x, y)

                    used_p = set(itertools.chain(r_p, c_p, s_p))
                    p = list(sorted(self.possible_values().difference(used_p)))

                    if p == []:
                        pprint(self.grille)
                        raise Exception(f"Cant solve puzzle -- x={x}, y={y}")
                    self.grille[y][x] = p[0]
        return self.grille
