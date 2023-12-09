"""
Our task is to perform flood fill by updating the values of the four
directionally connected cells, which have the same value as the source cell with the target value.
"""


def flood_fill(grid, sr, sc, target):
    starting_val = grid[sr][sc]
    flood_fill_rec(grid, sr, sc, starting_val, target)
    return grid


def flood_fill_rec(grid, row, col, starting_val, target):
    if (
        row < 0
        or row > len(grid)
        or col < 0
        or col > len(grid[0])
        or grid[row][col] != starting_val
        or grid[row][col] == target
    ):
        return

    grid[row][col] = target

    flood_fill_rec(grid, row + 1, col, starting_val, target)
    flood_fill_rec(grid, row - 1, col, starting_val, target)
    flood_fill_rec(grid, row, col + 1, starting_val, target)
    flood_fill_rec(grid, row, col - 1, starting_val, target)
