"""
Quick union with path halving i.e. making any element point to its grand parent.
"""


class QuickUnionPathHalving:
    def __init__(self, N):
        self.size = N
        self.n = [0] * self.size
        for i in range(self.size):
            self.n[i] = i

    def find_root(self, i):
        while i != self.n[i]:
            self.n[i] = self.n[
                self.n[i]
            ]  # this line points current element to its grand parent.
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
