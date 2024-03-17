"""
To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels.
"""


def flood_fill(grid, sr, sc, target):
    source = grid[sr][sc]
    flood_fill_rec(grid, sr, sc, source, target)
    return grid


def flood_fill_rec(grid, sr, sc, source, target):
    if (
        sr < 0
        or sr >= len(grid)
        or sc < 0
        or sc >= len(grid[0])
        or grid[sr][sc] != source
        or grid[sr][sc] == target
    ):
        return

    grid[sr][sc] = target

    flood_fill_rec(grid, sr + 1, sc, source, target)
    flood_fill_rec(grid, sr - 1, sc, source, target)
    flood_fill_rec(grid, sr, sc + 1, source, target)
    flood_fill_rec(grid, sr, sc - 1, source, target)


print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
