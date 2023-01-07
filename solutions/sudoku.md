# Sudoku -- examinator guide.



## col_possibilities
Attention points:
- detecting unsolved cell should be made by comparaison with the static variable 'UNDECLARED_CELL'
#### niv1
``` python
def col_possibilities(self, grid, x: int) -> list[int]:
    """use for loop with a variable for accumulating values"""
    result = []
    for row in grid:
        if row[x] > 0:
            result.append(row[x])
    return result
```

#### niv2
``` python
def col_possibilities(self, grid, x: int) -> list[int]:
    """use a for comprehension with a nested if"""
    return [row[x] for row in grid if row[x] > 0]
```

#### niv3
``` python
def col_possibilities(self, grid, x: int) -> list[int]:
    """use map and filter with lambda functions."""
    return sorted(
        filter(
            lambda x: x > UNDECLARED_CELL,
            map(lambda g: g[x], grid),
        )
    )
```

## row_possibilities
Attention points:
- detecting unsolved cell should be made by comparaison with the static variable 'UNDECLARED_CELL'
#### niv1
```python
def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
    """use for loop with a variable for accumulating values"""
    result = []
    for elements in grid[y]:
        if elements > 0:
            result.append(elements)
    return result
```
#### niv2
```python
def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
    """use a for comprehension with a nested if"""
    return [x for x in grid[y] if x > 0]
```
#### niv3
```python
def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
    """use map and filter with lambda functions."""
    return list(sorted(filter(lambda x: x != UNDECLARED_CELL, grid[y])))
```

## sector_possibilities
Attention points:
- :x: using ``reverse_sector_map()`` is highly recommend. Recomputing the sector cells each time is considered a bummer.
- :bulb: ``@functools.lru_cache`` : allow to put in cache the result of the function.
- :exclamation: detecting unsolved cell should be made by comparaison with the static variable 'UNDECLARED_CELL'.
- :exclamation: tests associated with this function are order aware. The candidat must search the reason for the tests failing. **Nota**: the correct test function is ``self.assertCountEqual``
#### niv1
```python
def sector_possibilities(self, grid: list[list[int]], coord_x: int, coord_y: int) -> list[int]:
    """use for loop with a variable for accumulating values."""
    result = []
    for cell_coords in self.reverse_sector_map()[(coord_x, coord_y)]:
        # x and y are flipped when accessing the initial grid du to the list of list.
        if grid[cell_coords[1]][cell_coords[0]] > 0:
            result.append(grid[cell_coords[1]][cell_coords[0]])
    return result

```
#### niv2
```python
def sector_possibilities(self, grid: list[list[int]], coord_x: int, coord_y: int) -> list[int]:
    """use a for comprehension with a nested if."""
    return [
        # x and y are flipped when accessing the initial grid du to the list of list.
        grid[cell_coords[1]][cell_coords[0]]
        for cell_coords in self.reverse_sector_map()[(coord_x, coord_y)]
        if grid[cell_coords[1]][cell_coords[0]] > 0
    ]
```
#### niv3
```python
def sector_possibilities(self, grid: list[list[int]], coord_x: int, coord_y: int) -> list[int]:
    """use map and filter with lambda functions."""
    return list(
        sorted(
            filter(
                lambda x: x > UNDECLARED_CELL,
                map(
                    # x and y are flipped when accessing the initial grid du to the list of list.
                    lambda x: grid[x[1]][x[0]],
                    self.reverse_sector_map()[(coord_x, coord_y)],
                ),
            )
        )
    )
```

## solve 

