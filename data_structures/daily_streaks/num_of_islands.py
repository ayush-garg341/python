"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water)
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

example1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

example2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

"""

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    num = 0
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "0":
                continue
            num += 1
            num_of_islands_rec(i, j, m, n, grid)

    return num


def num_of_islands_rec(row, column, m, n, grid):

    if row < 0 or row >= m:
        return 0
    if column < 0 or column >= n:
        return 0

    if grid[row][column] == "1":
        grid[row][column] = "0"
        num_of_islands_rec(row - 1, column, m, n, grid)
        num_of_islands_rec(row, column - 1, m, n, grid)
        num_of_islands_rec(row + 1, column, m, n, grid)
        num_of_islands_rec(row, column + 1, m, n, grid)


def numIslands_with_visited(grid: List[List[str]]) -> int:
    num = 0
    m = len(grid)
    n = len(grid[0])

    visited = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "0" or visited[i][j] == 1:
                continue
            num += 1
            num_of_islands_rec_with_visited(i, j, m, n, grid, visited)

    return num


def num_of_islands_rec_with_visited(row, column, m, n, grid, visited):
    if row < 0 or row >= m:
        return 0
    if column < 0 or column >= n:
        return 0

    if grid[row][column] == "1" and visited[row][column] == 0:
        visited[row][column] = 1
        num_of_islands_rec_with_visited(row - 1, column, m, n, grid, visited)
        num_of_islands_rec_with_visited(row, column - 1, m, n, grid, visited)
        num_of_islands_rec_with_visited(row + 1, column, m, n, grid, visited)
        num_of_islands_rec_with_visited(row, column + 1, m, n, grid, visited)


grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(numIslands_with_visited(grid_1))
print(numIslands_with_visited(grid_2))
print("======= num of islands when modifying input matrix ========")
print(numIslands(grid_1))
print(numIslands(grid_2))
