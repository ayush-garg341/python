"""
Find number of islands
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Using extra space as visited array
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        num = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == "1":
                    num += 1
                    self.dfs(r, c, grid, visited)
        return num

    def dfs(self, cr, cc, grid, visited):
        if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[0]):
            return
        if not visited[cr][cc] and grid[cr][cc] == "1":
            visited[cr][cc] = True
            self.dfs(cr + 1, cc, grid, visited)
            self.dfs(cr - 1, cc, grid, visited)
            self.dfs(cr, cc + 1, grid, visited)
            self.dfs(cr, cc - 1, grid, visited)

    def numIslandsWithoutSpace(self, grid: List[List[str]]) -> int:
        """
        Without any extra space
        """
        rows = len(grid)
        cols = len(grid[0])
        num = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num += 1
                    self.dfsWithoutSpace(r, c, grid)
        return num

    def dfsWithoutSpace(self, cr, cc, grid):
        if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[0]):
            return
        if grid[cr][cc] == "1":
            grid[cr][cc] = "0"
            self.dfsWithoutSpace(cr + 1, cc, grid)
            self.dfsWithoutSpace(cr - 1, cc, grid)
            self.dfsWithoutSpace(cr, cc + 1, grid)
            self.dfsWithoutSpace(cr, cc - 1, grid)


print("======= With extra space =========")
print(
    Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    Solution().numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)

print("======= Without extra space ====== ")
print(
    Solution().numIslandsWithoutSpace(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    Solution().numIslandsWithoutSpace(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
