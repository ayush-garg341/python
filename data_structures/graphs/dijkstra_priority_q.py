"""
Given a weighted, undirected and connected graph of V vertices.
 an adjacency list adj where adj[i] is a list of lists ( with weights )
You return a list of integers denoting shortest distance between each node
and Source vertex S.
"""

import heapq
import math


class Solution:
    def dijkstra(self, V, adj, S):
        dist = [math.inf] * V
        dist[S] = 0
        min_heap = []
        heapq.heappush(min_heap, (S, 0))
        while len(min_heap):
            vertex, d = heapq.heappop(min_heap)
            for adj_v in adj[vertex]:
                adj_d, adj_vertex = adj_v[1], adj_v[0]
                if adj_d + d < dist[adj_vertex]:
                    dist[adj_vertex] = adj_d + d
                    heapq.heappush(min_heap, (adj_vertex, adj_d + d))

        return dist


soln = Solution()
print(soln.dijkstra(3, [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], 2))
print(soln.dijkstra(2, [[[1, 9]], [[0, 9]]], 0))
