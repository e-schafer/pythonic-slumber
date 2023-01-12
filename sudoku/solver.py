import functools
import itertools
import re
from collections import deque
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
        """
        # TODO: implement this method
        pass

    def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
        """List the already used values on the row.

        grid -- the sudoku grid to analyze
        coord_y -- y coordinate
        """
        # TODO
        pass

    def sector_possibilities(
        self, grid: list[list[int]], coord_x: int, coord_y: int
    ) -> list[int]:
        """List the already used values in the sector.

        grid -- the sudoku grid to analyze
        coord_x -- x coordinate
        coord_y -- y coordinate
        """
        # TODO
        pass

    def is_valid(
        self, grid: list[list[int]], x: int, y: int, val_to_check: int
    ) -> bool:
        """Check if a value can be used.

        grid -- the sudoku grid
        x -- x coord
        y -- y coord
        val_to_check -- the value to check (1 to 9)
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
        # TODO
        pass
