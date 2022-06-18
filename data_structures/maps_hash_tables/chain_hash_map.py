from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """
    Hash map implemented with separate chaining
    """

    def _bucket_getitem(self, j, key):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(key))
        return bucket[key]

    def _bucket_setitem(self, j, key, val):
        bucket = self._table[j]
        old_size = len(self._table[j])
        if bucket is None:
            bucket = UnsortedTableMap()
            bucket[key] = val
            self._table[j] = bucket
        else:
            bucket[key] = val

        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, key):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(key))
        del bucket[key]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for (k, v) in bucket:
                    yield k
