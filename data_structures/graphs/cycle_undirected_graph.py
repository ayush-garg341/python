"""
Detect cycle in undirected graph using BFS and DFS
"""

from typing import List
from queue import Queue


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        parent = [0] * V
        # Graph might be disconnected
        # Need to cover all vertices
        for v in range(V):
            if not visited[v]:
                exist = self.isCycleBFS(v, adj, visited, parent)
                if exist:
                    return True

        return False

    def isCycleBFS(
        self, v: int, adj: List[List[int]], visited: List[int], parent: List[int]
    ) -> bool:
        # Running BFS on each disconnected component
        q = Queue()
        q.put(v)
        visited[v] = True
        parent[v] = v
        while not q.empty():
            node = q.get()
            for v in adj[node]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = node
                    q.put(v)
                else:
                    if parent[node] != v:
                        return True

        return False


print(Solution().isCycle(5, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))

print(Solution().isCycle(4, [[], [2], [1, 3], [2]]))
