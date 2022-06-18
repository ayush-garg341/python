from collections import MutableMapping


class MapBase(MutableMapping):
    """
    Our own abstract base class that includes non public _item class.
    """

    class _Item:
        """
        Lighweight composite to store key value pairs as map items.
        """

        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self._key == other._key)

        def __lt__(self, other):
            return self._key < other._key
