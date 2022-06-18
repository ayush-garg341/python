from map_base import MapBase
from random import randrange
from abc import abstractmethod


class HashMapBase(MapBase):
    """
    Generic parent class for separate chaining and linear probing sub-class.
    """

    def __init__(self, cap=11, p=23):
        self._table = cap * [None]  # initializing the hash map with size = 12
        self._n = 0  # count of distinct key value pairs
        self._prime = p  # prime number
        self._scale = 1 + randrange(p - 1)  # scale from 1 tp p-1
        self._shift = randrange(p)  # scale from 0 to p-1

    @abstractmethod
    def _bucket_setitem(self, j, k, v):
        """
        Subclasses must implement the method
        """
        pass

    @abstractmethod
    def _bucket_getitem(self, j, k):
        """
        Subclasses must implement the method
        """
        pass

    @abstractmethod
    def _bucket_delitem(self, j, k):
        """
        Subclasses must implement the method
        """
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def hash(self, key):
        return (self._scale * hash(key) + self._shift) % self._prime % len(self._table)

    def __setitem__(self, key, value):
        j = self.hash(key)
        self._bucket_setitem(j, key, value)
        if self._n > len(self._table) // 2:  # keep load factor < 0.5
            self._resize(2 * len(self._table) - 1)

    def __getitem__(self, key):
        j = self.hash(key)
        return self._bucket_getitem(j, key)

    def __delitem__(self, key):
        j = self.hash(key)
        self._bucket_delitem(j, key)
        self._n -= 1

    def __len__(self):
        return self._n

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0  # n re-computed during set
        for (k, v) in old:
            self[k] = v  # calls the __setitem__ internally
