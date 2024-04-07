class Solution:
    def isCyclic(self, V, adj):
        visited = [0] * V
        path_visited = [0] * V
        for v in range(V):
            if not visited[v]:
                visited[v] = 1
                path_visited[v] = 1
                has_cycle = self.dfs(v, adj, visited, path_visited)
                if has_cycle:
                    return True

        return False

    def dfs(self, curr_v, adj, visited, path_visited):
        for v in adj[curr_v]:
            if not visited[v]:
                visited[v] = 1
                path_visited[v] = 1
                ret = self.dfs(v, adj, visited, path_visited)
                if ret:
                    return ret
            else:
                if path_visited[v]:
                    return True

        path_visited[curr_v] = 0


soln = Solution()
print(soln.isCyclic(4, [[1], [2], [3], [3]]))
print(soln.isCyclic(3, [[1], [2], []]))
