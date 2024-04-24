"""
Modified version of BFS

- Calculate indegree of nodes
- Put nodes with indegree 0 in queue
- Take out an element from queue and iterate over adjacent nodes

- Can use this algo to detect cycle
- If toposort has less than N vertices, it means there is
    some problem biggest of which is cycle
"""


class Solution:
    def topoSort(self, V, adj):
        toposort = []
        indegree = [0] * V
        for adjlist in adj:
            for elt in adjlist:
                indegree[elt] += 1

        q = []
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        while q:
            elt = q.pop(0)
            toposort.append(elt)
            for adjv in adj[elt]:
                indegree[adjv] -= 1
                if indegree[adjv] == 0:
                    q.append(adjv)

        return toposort


soln = Solution()
print(soln.topoSort(4, [[], [0], [0], [0]]))
