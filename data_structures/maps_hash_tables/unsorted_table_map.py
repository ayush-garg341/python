from map_base import MapBase


class UnsortedTableMap(MapBase):
    """
    Map implementation using an un-ordered list.
    """

    def __init__(self):
        """
        Create an empty map
        """
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if item._key == key:
                return item._value
        raise KeyError("Key Error: " + repr(key))

    def __setitem__(self, key, value):
        for item in self._table:
            if item._key == key:
                item._value = value
                return

        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        for i in range(len(self._table)):
            item = self._table[i]
            if item._key == key:
                self._table.pop(i)
                return

        raise KeyError("Key Error: " + repr(key))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key
