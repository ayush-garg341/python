from .pq_abc import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """
    A min-oriented priority queue implemented with binary heap.
    """

    def __init__(self, contents=()):
        """
        Create a new empty Priority Queue.
        """
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        """
        Bottom up heap construction runs in O(n) given an iterable
        """
        start = self._parent(len(self._data) - 1)
        for i in range(start, -1, -1):
            self._downheap(i)

    def __len__(self):
        """
        Return the length of priority queue.
        """
        return len(self._data)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """
        Swap the elements at indices i and j
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """
        Upheap in case of inserting new element.
        """
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        """
        Down heap in case of removing min element.
        """
        if self._has_left(j):
            left = self._left(j)
            small_child = left

            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[j] > self._data[small_child]:
                self._swap(small_child, j)
                self._downheap(small_child)

    def add(self, key, value):
        """
        Add a key-value pair to priority queue.
        """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        """
        Return the min element from priority queue.
        """
        if self.is_empty():
            raise Exception("Prioity Queeu is empty")

        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove and return the min element from pq.
        """
        if self.is_empty():
            raise Exception("Prioity queue is empty")

        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
