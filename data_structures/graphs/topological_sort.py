class Solution:

    def topoSort(self, V, adj):
        visited = [0] * V
        stack = []
        for v in range(V):
            if not visited[v]:
                visited[v] = 1
                self.dfs(v, adj, visited, stack)

        stack.reverse()
        return stack

    def dfs(self, currv, adj, visited, stack):
        for adjv in adj[currv]:
            if not visited[adjv]:
                visited[adjv] = 1
                self.dfs(adjv, adj, visited, stack)

        stack.append(currv)


soln = Solution()
print(soln.topoSort(4, [[], [0], [0], [0]]))
