"""
Check if a graph is bipartite i.e 2-colorable
"""


class Solution:
    def isBipartiteBFS(self, V, adj):
        colors = [-1] * V
        q = []
        for v in range(V):
            if colors[v] == -1:
                q.append(v)
                colors[v] = 1
                while len(q):
                    v = q.pop()
                    for adj_v in adj[v]:
                        if colors[adj_v] == -1:
                            colors[adj_v] = 1 - colors[v]
                            q.append(adj_v)
                        else:
                            if colors[adj_v] == colors[v]:
                                return False
        return True

    def isBipartiteDFS(self, V, adj):
        colors = [-1] * V
        for v in range(V):
            if colors[v] == -1:
                colors[v] = 0
                ret = self.isBipartiteDFSRec(colors, adj, v)
                if not ret:
                    return False
        return True

    def isBipartiteDFSRec(self, colors, adj, v):
        for adjv in adj[v]:
            if colors[adjv] == -1:
                colors[adjv] = 1 - colors[v]
                ret = self.isBipartiteDFSRec(colors, adj, adjv)
                if not ret:
                    return False
            else:
                if colors[adjv] == colors[v]:
                    return False
        return True

soln = Solution()
# print(soln.isBipartiteBFS(3, [[1], [2], []]))
print(soln.isBipartiteDFS(3, [[1], [2], []]))
