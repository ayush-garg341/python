"""
find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island.
"""

from typing import List

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        distinct_islands = set()
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    tup = []
                    self.dfs(r, c, grid, tup, visited, r, c)
                    distinct_islands.add(tuple(tup))
        return len(distinct_islands)

    def dfs(self, cr:int, cc:int, grid: List[List[int]], tup: tuple, vis: List[List[int]], baser:int, basec:int):
        if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[0]) or vis[cr][cc]:
            return

        if grid[cr][cc] == 1 and not vis[cr][cc]:
            vis[cr][cc] = 1
            tup.append((cr-baser, cc-basec))
            self.dfs(cr+1, cc, grid, tup, vis, baser, basec)
            self.dfs(cr-1, cc, grid, tup, vis, baser, basec)
            self.dfs(cr, cc+1, grid, tup, vis, baser, basec)
            self.dfs(cr, cc-1, grid, tup, vis, baser, basec)


print(Solution().countDistinctIslands(
    [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
))

print(Solution().countDistinctIslands(
    [[1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]]
))
