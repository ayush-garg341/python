"""
Quick find implements two methods:-
    1. connected(p, q) -> to check if p and q are in same component.
    2. union(p, q) -> merge components containing p and q.
"""


class QuickFind:
    def __init__(self, N):
        self.size = N
        self.n = [0] * self.size
        for i in range(self.size):
            self.n[i] = i

    def quick_find(self, p, q):
        return self.n[p] == self.n[q]

    def union(self, p, q):
        id_p = self.n[p]
        id_q = self.n[q]

        for i in range(self.size):
            if self.n[i] == id_p:
                self.n[i] = id_q
