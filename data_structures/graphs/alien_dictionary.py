"""
Rather than creating normal human dictionary,
sort the alphabets according to alien words.
"""


class Solution:
    def findOrder(self, alien_dict, N, K):
        order = []
        adjlist = [[] for i in range(K)]
        for i in range(N - 1):
            w1 = alien_dict[i]
            w2 = alien_dict[i + 1]
            size = min(len(w1), len(w2))
            for j in range(size):
                if w1[j] != w2[j]:
                    idx1 = ord(w1[j]) % 97
                    idx2 = ord(w2[j]) % 97
                    adjlist[idx1].append(idx2)
                    break

        q = []
        indegree = [0] * K
        for i in range(len(adjlist)):
            for adj_v in adjlist[i]:
                indegree[adj_v] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.pop(0)
            char = chr(97 + node)
            order.append(char)
            for adj_v in adjlist[node]:
                indegree[adj_v] -= 1
                if indegree[adj_v] == 0:
                    q.append(adj_v)

        return order


soln = Solution()
print(soln.findOrder(["baa", "abcd", "abca", "cab", "cad"], 5, 4))
print(soln.findOrder(["caa", "aaa", "aab"], 3, 3))
