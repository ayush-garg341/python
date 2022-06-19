"""
Examine each node on the path to root. And set the parent of each node as root, so that tree remains almost flat.
"""


class QuickUnionPathCompression:
    def __init__(self, N):
        self.size = N
        self.n = [0] * self.size
        for i in range(self.size):
            self.n[i] = i

    def find_root(self, i):
        root = i
        while root != self.n[root]:
            root = self.n[root]

        while i != root:
            temp = self.n[i]
            self.n[i] = root
            i = temp

        return root

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def union(self, p, q):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if p_root == q_root:
            return
        self.n[p_root] = q_root
