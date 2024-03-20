"""
Given an m x n matrix board containing 'X' and 'O', capture all regions
that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for c in range(cols)] for r in range(rows)]

        # traverse for all boundary values

        # traverse for row 0
        for c in range(cols):
            if not visited[0][c]:
                self.dfs(board, rows, cols, 0, c, visited)

        # traverse for col 0
        for r in range(1, rows):
            if not visited[r][0]:
                self.dfs(board, rows, cols, r, 0, visited)

        # traverse for last row
        for c in range(1, cols):
            if not visited[rows - 1][c]:
                self.dfs(board, rows, cols, rows - 1, c, visited)

        # tranverse for last column
        for r in range(1, rows - 1):
            if not visited[r][cols - 1]:
                self.dfs(board, rows, cols, r, cols - 1, visited)

        # traverse for internal elements
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"

        return board

    def dfs(self, board, rows, cols, r, c, visited):
        # Check this condition carefully as it can lead to max recursion depth
        if r < 0 or r >= rows or c < 0 or c >= cols and visited[r][c]:
            return

        visited[r][c] = 1

        if board[r][c] == "O":
            self.dfs(board, rows, cols, r + 1, c, visited)
            self.dfs(board, rows, cols, r - 1, c, visited)
            self.dfs(board, rows, cols, r, c + 1, visited)
            self.dfs(board, rows, cols, r, c - 1, visited)


print(
    Solution().solve(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)

print(Solution().solve([["X"]]))
