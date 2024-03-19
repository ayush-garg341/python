"""
Given an m x n binary matrix mat, return the distance of the
nearest 0 for each cell.

kernprof -lv data_structures/graphs/nearest_distance_0.py
pip install line_profiler
"""

# from queue import Queue
from collections import deque
from typing import List


class Solution:
    # @profile
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        q = deque()
        nearest_distance = [[-1 for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    nearest_distance[r][c] = 0
                    q.append((r, c, 0))

        while len(q):
            r, c, dist = q.popleft()
            if r + 1 < rows and mat[r + 1][c] == 1 and nearest_distance[r + 1][c] == -1:
                nearest_distance[r + 1][c] = dist + 1
                q.append((r + 1, c, dist + 1))

            if r - 1 >= 0 and mat[r - 1][c] == 1 and nearest_distance[r - 1][c] == -1:
                nearest_distance[r - 1][c] = dist + 1
                q.append((r - 1, c, dist + 1))

            if c + 1 < cols and mat[r][c + 1] == 1 and nearest_distance[r][c + 1] == -1:
                nearest_distance[r][c + 1] = dist + 1
                q.append((r, c + 1, dist + 1))

            if c - 1 >= 0 and mat[r][c - 1] == 1 and nearest_distance[r][c - 1] == -1:
                nearest_distance[r][c - 1] = dist + 1
                q.append((r, c - 1, dist + 1))

        return nearest_distance


if __name__ == "__main__":
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
