class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        dfs = []
        visited[0] = True
        self.dfs_rec(0, adj, visited, dfs)
        return dfs

    def dfs_rec(self, cv, adj, visited, dfs):
        dfs.append(cv)
        for v in adj[cv]:
            if not visited[v]:
                visited[v] = True
                self.dfs_rec(v, adj, visited, dfs)


soln = Solution()
print(soln.dfsOfGraph(5, [[2, 3, 1], [0], [0, 4], [0], [2]]))
