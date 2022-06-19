"""
Quick union also have same two methods.
    1. connected(p, q) -> check if p and q have same root.
    2. union(p, q) -> id of p's root equals to id of q's root.

id[i] is parent of i, and if i == id[i] it means that i is root position.
Take size into account and try to put smaller tree under larger tree, so that balance maintains.
"""


class WeightedQuickUnion:
    def __init__(self, N):
        self.size = N
        self.n = [0] * self.size
        self.tree_size = [1] * self.size
        for i in range(self.size):
            self.n[i] = i

    def find_root(self, i):
        while i != self.n[i]:
            i = self.n[i]
        return i

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
