from hash_map_base import HashMapBase


class ProbleHashMap(HashMapBase):
    """
    Hash map implemented using linear probling to avoid collisions.
    """

    _AVAIL = object()  # sentinal marks locations of previous deletions

    def _is_available(self, j):
        """
        Return True if index j is available in table.
        """

        return self._table[j] is None or self._table[j] is ProbleHashMap._AVAIL

    def _find_slot(self, j, k):
        """
        Search for key k in bucket at index j

        Return (success, index) tuple
        if match was found, success is True and index denotes its location.
        if no match found, success is False and index denotes its first available slot.
        """

        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j
                if self._table[j] is None:  # search has failed
                    return (False, first_avail)
            elif k == self._table[j]._key:  # found a match
                return (True, j)

            j = (j + 1) % len(self._table)  # look cyclically

    def _bucket_getitem(self, j, key):
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError("Key Error :" + repr(key))
        return self._table[s]._value

    def _bucket_setitem(self, j, key, value):
        found, s = self._find_slot(j, key)
        if not found:
            self._table[s] = self._Item(key, value)
            self._n += 1
        else:
            self._table[s]._value = value

    def _bucket_delitem(self, j, key):
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError("Key Error : " + repr(key))
        self._table[s] = ProbleHashMap._AVAIL

    def __iter__(self):
        for (k, v) in self._table:
            if v is not None and v is not ProbleHashMap._AVAIL:
                yield k
