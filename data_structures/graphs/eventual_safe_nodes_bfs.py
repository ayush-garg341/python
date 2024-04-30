"""
Terminal node is safe node.
All paths from a node leads to terminal node.

- Outgoing num of edge = 0
- Reverse the graph
- Run topo sort as usual with help of queue
- Sort the output and return
"""

from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []
        q = deque()
        indegree = [0] * len(graph)
        graph = self.reverse(graph)
        for adjlist in graph:
            for adjv in adjlist:
                indegree[adjv] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            safe_nodes.append(node)
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        safe_nodes.sort()
        return safe_nodes

    def reverse(self, graph: List[List[int]]) -> List[List[int]]:
        new_graph = [[] for i in range(len(graph))]
        for i in range(len(graph)):
            for adjv in graph[i]:
                new_graph[adjv].append(i)

        return new_graph


soln = Solution()
print(soln.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(soln.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
