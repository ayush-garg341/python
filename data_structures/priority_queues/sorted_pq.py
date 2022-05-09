"""
Implementing pq with sorted list.
"""

from .pq_abc import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
    """
    A min oriented pq with sorted list
    """

    def __init__(self):
        """
        Create a new empty Priority Queue.
        """
        self._data = PositionalList()

    def __len__(self):
        """
        Return the number of items in priority queue.
        """
        return len(self._data)

    def add(self, key, value):
        """
        Add a key value pair.
        """
        newest = self._Item(key, value)
        walk = self._data.last()  # walk backward and looking for smaller key
        while walk is not None and walk.element() > newest:
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)  # newest key is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        """
        Return but do not remove (k, v) tuple with minimum key
        """
        if self.is_empty():
            raise Empty("Priorty queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove and return (k, v) with minimum key
        """
        if self.is_empty():
            raise Empty("Priority Queue is empty")

        item = self._data.delete(self._data.first())
        return (item._key, item._value)
