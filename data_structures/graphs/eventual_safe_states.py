"""
- Graph should not have a cycle.
- Any outgoing edge from a node to a part of cycle
"""

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []
        visited = [0] * len(graph)
        path_visited = [0] * len(graph)
        V = len(graph)
        for v in range(V):
            if not visited[v]:
                visited[v] = 1
                path_visited[v] = 1
                self.dfs(v, graph, visited, path_visited, safe_nodes)

        safe_nodes.sort()
        return safe_nodes

    def dfs(self, v, graph, visited, path_visited, safe_nodes):
        for adjv in graph[v]:
            if not visited[adjv]:
                visited[adjv] = 1
                path_visited[adjv] = 1
                ret = self.dfs(adjv, graph, visited, path_visited, safe_nodes)
                if ret:
                    return True
            else:
                if path_visited[adjv]:
                    return True

        path_visited[v] = 0
        safe_nodes.append(v)


soln = Solution()
print(soln.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(soln.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
