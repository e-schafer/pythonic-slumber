from pprint import pprint

from solver import Sudoku


grille1 = [
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


if __name__ == "__main__":
    sudoku = Sudoku(grille=grille1, size=3)
    # pprint(sudoku.reverse_sector_map()[0, 8])
    pprint(sudoku.sector_possibilities(0, 8))
    pprint(
        list(
            map(
                lambda x: f"{x[0]}:{x[1]} -- {grille1[x[1]][x[0]]}",
                sudoku.reverse_sector_map()[(0, 8)],
            )
        )
    )
