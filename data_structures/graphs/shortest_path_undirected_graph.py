"""
Undirected graph with unit weights
Can use BFS as order does not matter.
"""

import math


class Solution:
    def shortestPath(self, edges, n, m, src):
        adj_list = [[] for i in range(n)]
        for edge in edges:
            source = edge[0]
            dst = edge[1]
            adj_list[source].append(dst)
            adj_list[dst].append(source)

        visited = [0] * n
        q = []
        distance = [math.inf] * n
        distance[src] = 0
        visited[src] = 1
        q.append(src)

        while q:
            node = q.pop(0)
            for adj in adj_list[node]:
                if not visited[adj]:
                    visited[adj] = 1
                    q.append(adj)
                    distance[adj] = min(distance[node] + 1, distance[adj])

        for i in range(n):
            if distance[i] == math.inf:
                distance[i] = -1
        return distance


soln = Solution()
print(
    soln.shortestPath(
        [
            [0, 1],
            [0, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [1, 2],
            [2, 6],
            [6, 7],
            [7, 8],
            [6, 8],
        ],
        9,
        10,
        0,
    )
)
print(soln.shortestPath([[0, 0], [1, 1], [1, 3], [3, 0]], 4, 4, 3))
