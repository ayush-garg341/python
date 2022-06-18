from map_base import MapBase


class SortedMapTable(MapBase):
    """
    Map implementation using a sorted table.
    """

    def __init__(self):
        """
        Create an mt map
        """
        self._table = []

    def __len__(self):
        return len(self._table)

    def _find_index(self, k, low, high):
        """
        Performs a binary search
        """
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)

            else:
                return self._find_index(k, mid + 1, high)

    def __getitem__(self, k):
        index = self._find_index(k, 0, len(self._table) - 1)
        if index == len(self._table) or self._table[index]._key != k:
            raise KeyError("Key Error : " + repr(k))
        return self._table[index]._value

    def __setitem__(self, k, v):
        index = self._find_index(k, 0, len(self._table) - 1)
        if self._table[index]._key == k:
            self._table[index]._value = v
        else:
            self._table.insert(index, self._Item(k, v))

    def __delitem__(self, k):
        index = self._find_index(k, 0, len(self._table) - 1)
        if index == len(self._table) or self._table[index]._key == k:
            raise KeyError("Key Error : " + repr(k))
        self._table.pop(index)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        index = self._find_index(k, 0, len(self._table) - 1)
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        else:
            return None

    def find_gt(self, k):
        index = self._find_index(k, 0, len(self._table) - 1)
        if index < len(self._table) and self._table[index]._key == k:
            index += 1
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        else:
            return None

    def find_lt(self, k):
        index = self._find_index(k, 0, len(self._table) - 1)
        if index > 0:
            return (self._table[index]._key, self._table[index]._value)
        else:
            return None

    def find_range(self, start, stop):
        """
        Iterate through all (key, value) pairs such that start <= key < stop.

        if start is None, iteration begins with minimum key of map.
        if stop is None, iteration continues through the maximum key of map
        """

        if start is None:
            index = 0
        else:
            index = self._find_index(start, 0, len(self._table) - 1)

        while index < len(self._table) and (stop is None or self._table[index]._key < stop):
            yield (self._table[index]._key, self._table[index]._value)
            index += 1
