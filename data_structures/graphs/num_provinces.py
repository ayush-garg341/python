"""
Find number of provinces connected
Two ways:
- Adj list and then dfs
- Union Find
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = [[] for num in range(n)]

        # Converting to adjacency list first and then running dfs
        for r in range(n):
            for c in range(r + 1, n):
                if isConnected[r][c]:
                    adj_list[r].append(c)
                    adj_list[c].append(r)

        visited = [False for i in range(n)]
        num = 0
        for v in range(n):
            if not visited[v]:
                num += 1
                visited[v] = True
                self.dfs(v, adj_list, visited)

        return num

    def dfs(self, root, adj_list, visited):
        for v in adj_list[root]:
            if not visited[v]:
                visited[v] = True
                self.dfs(v, adj_list, visited)


print(
    Solution().findCircleNum(
        [
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        ]
    )
)
