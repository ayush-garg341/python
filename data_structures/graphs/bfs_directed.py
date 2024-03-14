from typing import List
from queue import Queue


class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        bfs = []
        q = Queue()
        q.put(0)
        vis = [False] * V
        vis[0] = True

        while not q.empty():
            v = q.get()
            bfs.append(v)
            for adj_v in adj[v]:
                if not vis[adj_v]:
                    vis[adj_v] = True
                    q.put(adj_v)
        return bfs


soln = Solution()
print(soln.bfsOfGraph(5, [[1, 2, 3], [], [4], [], []]))
