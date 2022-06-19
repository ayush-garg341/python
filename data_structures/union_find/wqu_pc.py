"""
Weighted quick union with path compression.
This algorithm practically runs in linear time and most optmizied.
"""


class WeightedQuickUnionPathCompression:
    def __init__(self, N):
        self.size = N
        self.n = [0] * self.size
        self.tree_size = [1] * self.size
        for i in range(self.size):
            self.n[i] = i

    def validate(self, p):
        if p < 0 or p >= self.size:
            raise Exception("Invalid element position")

    def find_root(self, i):
        self.validate(i)
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

        if self.tree_size[p_root] < self.tree_size[q_root]:
            self.n[p_root] = q_root
            self.tree_size[q_root] += self.tree_size[p_root]
        else:
            self.n[q_root] = p_root
            self.tree_size[p_root] += self.tree_size[q_root]
