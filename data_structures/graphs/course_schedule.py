"""
Correct ordering for task completion.
Use BFS/topo sort to get order
"""

from timer import my_timer
from collections import deque


class Solution:
    @my_timer
    def findOrder(self, n, m, prerequisites):
        graph = [[] for i in range(n)]
        for task in prerequisites:
            graph[task[0]].append(task[1])
        q = deque()
        order = []
        indegree = [0] * n
        for adjlist in graph:
            for elt in adjlist:
                indegree[elt] += 1

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            task = q.popleft()
            order.append(task)
            for adj in graph[task]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        if len(order) == n:
            return order
        return []


soln = Solution()
print(soln.findOrder(2, 1, [[1, 0]]))
print(soln.findOrder(4, 4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
