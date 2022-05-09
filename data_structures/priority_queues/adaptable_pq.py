"""
Adaptable Priority Queue must support the following additional ops:
    - Removing the element with arbitrary priority not just with min priority (remove_min).
    - Updating the priority of an element i.e. replacing the key of an existing entry with new key.

P.update(loc, k, v) -> replace the key and value for the item identified by locator loc.
P.remove(loc) -> Remove the item identified by loc from pq and return its (k, v).
"""

from .binary_heap import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):
    """
    A locator based priority queue implemented with binary heap.
    """

    class Locator(HeapPriorityQueue._Item):
        """
        Token for locating an entry of priority queue.
        """

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, i, j):
        super().swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, k, v) -> Locator:
        token = self.Locator(k, v, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, new_key, new_val):
        """
        Update key and value identified by locator loc.
        """
        j = loc._index
        if not (0 <= j and j < len(self) and self._data[j] is loc):
            raise Exception("Invalid Locator")
        token = self.Locator(new_key, new_val, j)
        self._data[j] = token
        self._bubble(j)

    def remove(self, loc):
        """
        Remove the entry with locator loc.
        """
        idx = loc._index
        if not (0 <= idx and idx < len(self) and self._data[idx] is loc):
            raise Exception("Invalid Locator")
        if idx == len(self._data) - 1:
            self._data.pop()
        else:
            last = len(self._data) - 1
            self._swap(idx, last)
            self._data.pop()
            self._bubble(idx)
            return (loc._key, loc._value)
