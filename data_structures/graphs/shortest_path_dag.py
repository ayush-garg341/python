"""
- Create weighted adjacency list
- Run topo sort using dfs
- From topo sort, calculate distance using adj list
"""

from typing import List
import math


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        distance = []
        adj_list = []
        topo_sort = []
        visited = []
        for i in range(n):
            adj_list.append([])
            distance.append(math.inf)
            visited.append(0)

        distance[0] = 0

        for edge in edges:
            src = edge[0]
            dest = edge[1]
            weight = edge[2]
            adj_list[src].append([dest, weight])

        for v in range(n):
            if not visited[v]:
                visited[v] = 1
                self.dfs(adj_list, visited, topo_sort, v)

        while topo_sort:
            node = topo_sort.pop()
            dist = distance[node]
            for adj_v in adj_list[node]:
                dest = adj_v[0]
                weight = adj_v[1]
                distance[dest] = min(distance[dest], dist + weight)

        for i in range(n):
            if distance[i] == math.inf:
                distance[i] = -1

        return distance

    def dfs(self, adj_list, visited, topo_sort, current_v):
        for adj_v in adj_list[current_v]:
            dest = adj_v[0]
            if not visited[dest]:
                visited[dest] = 1
                self.dfs(adj_list, visited, topo_sort, dest)

        topo_sort.append(current_v)


soln = Solution()
print(soln.shortestPath(4, 2, [[0, 1, 2], [0, 2, 1]]))
print(
    soln.shortestPath(
        6,
        7,
        [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]],
    )
)
