# col_possibilities
### niv1
``` python
def col_possibilities(self, grid, x: int) -> list[int]:
    """use for loop with a variable for accumulating values"""
    result = []
    for row in grid:
        if row[x] > 0:
            result.append(row[x])
    return result
```

### niv2
``` python
def col_possibilities(self, grid, x: int) -> list[int]:
    """use a for comprehension with a nested if"""
    return [row[x] for row in grid if row[x] > 0]
```
### niv3
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

# row_possibilities
### niv1
```python
def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
    """use for loop with a variable for accumulating values"""
    result = []
    for elements in grid[y]:
        if elements > 0:
            result.append(elements)
    return result
```
### niv2
```python
def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
    """use a for comprehension with a nested if"""
    return [x for x in grid[y] if x > 0]
```
### niv3
```python
def row_possibilities(self, grid: list[list[int]], y: int) -> list[int]:
    """use map and filter with lambda functions."""
    return list(sorted(filter(lambda x: x != UNDECLARED_CELL, grid[y])))
```

# sector_possibilities
### niv1
### niv2
### niv3

# solve