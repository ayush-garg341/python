"""
Quick union also have same two methods.
    1. connected(p, q) -> check if p and q have same root.
    2. union(p, q) -> id of p's root equals to id of q's root.

id[i] is parent of i, and if i == id[i] it means that i is root position.
"""


class QuickUnion:
    def __init__(self, N):
        self.size = N
        self.n = [0] * self.size
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
        self.n[p_root] = q_root
