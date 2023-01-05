from collections import deque
import functools
import itertools
from pprint import pprint

UNDECLARED_CELL = 0


class Sudoku:
    def __init__(self, size: int):
        self.size = size
        self.result_grid: list[list[int]] = []

    @functools.lru_cache
    def sector_map(self) -> dict[int, list[tuple[int, int]]]:
        """Create une dict mapping a sector to all coordinates inside the sector"""
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
        """Create a dict which map a location to all the locations inside the same sector"""
        dict_coord = {}
        for key, value in self.sector_map().items():
            for coord in value:
                dict_coord[coord] = value
        return dict_coord

    def col_possibilities(self, grid, x: int) -> list[int]:
        """List the already used values on the column.

        grid -- the sudoku grid to analyze
        coord_x -- x coordinate
        --------------------------------------
        niv1 : use for loop with a variable for accumulating values
        niv2 : use a for comprehension with a nested if
        niv3 : use map and filter
        niv4 : use map and filter with lambda functions.
        """
        return sorted(
            filter(
                lambda x: x > UNDECLARED_CELL,
                map(lambda i: grid[i][x], range(0, self.size**2)),
            )
        )

    def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
        """List the already used values on the row.

        grid -- the sudoku grid to analyze
        coord_y -- y coordinate
        --------------------------------------
        niv1 : use for loop with a variable for accumulating values
        niv2 : use a for comprehension with a nested if
        niv3 : use map and filter
        niv4 : use map and filter with lambda functions.
        """
        return list(sorted(filter(lambda x: x != UNDECLARED_CELL, grid[y])))

    def sector_possibilities(
        self, grid: list[list[int]], coord_x: int, coord_y: int
    ) -> list[int]:
        """List the already used values in the sector.

        grid -- the sudoku grid to analyze
        coord_x -- x coordinate
        coord_y -- y coordinate
        --------------------------------------
        niv1 : use for loop with a variable for accumulating values
        niv2 : use a for comprehension with a nested if
        niv3 : use map and filter
        niv4 : use map and filter with lambda functions.
        """
        return list(
            sorted(
                filter(
                    lambda x: x > UNDECLARED_CELL,
                    map(
                        # x and y are flipped when accessing the initial grid du to the list of list
                        lambda x: grid[x[1]][x[0]],
                        self.reverse_sector_map()[(coord_x, coord_y)],
                    ),
                )
            )
        )

    def is_valid(
        self, grid: list[list[int]], x: int, y: int, val_to_check: int
    ) -> bool:
        """Check if a value can be used.

        grid -- the sudoku grid
        x -- x coord
        y -- y coord
        val_to_check -- the value to check (1 to 9)
        --------------------------------------
        niv1 : use add operator
        niv2 : use sum
        niv3 : use itertools
        + 0.5niv: if use a set
        """
        return val_to_check not in set(
            itertools.chain(
                self.row_possibilities(grid, y),
                self.col_possibilities(grid, x),
                self.sector_possibilities(grid, x, y),
            )
        )

    def solve_grid(self, grid: list[list[int]], x: int = 0, y: int = 0) -> bool:
        """Solve the grid by using backtrackings

        grid -- sudoku grid to solve
        x -- x coord for the current position
        y -- y coord for the current position
        """
        self.result_grid = grid
        next_y, next_x = divmod((x + 1) + (y * self.size**2), self.size**2)
        if x >= self.size**2 or y >= self.size**2:
            return True
        if grid[y][x] == 0:
            for val in range(1, self.size**2 + 1):
                if self.is_valid(grid, x, y, val):
                    grid[y][x] = val
                    if self.solve_grid(grid, next_x, next_y):
                        return True
                    grid[y][x] = 0
        else:
            if self.solve_grid(grid, next_x, next_y):
                return True
        return False
