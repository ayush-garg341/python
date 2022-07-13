"""
When given range queries on an array, it' better to make the segment tree out of it.
Then perform range queries.
"""

import math


class SegmentTree:
    """
    Creating a min segment tree.
    """

    def __init__(self, array):
        """
        Initializing segment tree array of appropriate size.
        """
        self.array = array
        self.size = len(array)
        self.st_size = 2 * self.size - 1
        self.st_array = [0 for i in range(self.st_size)]

    def create_st_array(self, low, high, pos):
        """
        Populating segment tree array with appropriate values recursively.
        """
        if low == high:
            self.st_array[pos] = self.array[low]
            return

        mid = (low + high) // 2
        self.create_st_array(low, mid, 2 * pos + 1)
        self.create_st_array(mid + 1, high, 2 * pos + 2)

        self.st_array[pos] = min(self.st_array[2 * pos + 1], self.st_array[2 * pos + 2])

    def search_st_array(self, q_low, q_high, low, high, pos):
        """
        Search minimum in the given range of an original array.
        Three major conditions
            1. Complete overlap, return the value at that node.
            2. Partial Overlap, go in left and right subtree.
            3. No overlap, return max value in case we are finding min value.
        """

        # Complete overlap
        if q_low <= low and q_high >= high:
            return self.st_array[pos]

        # No overlap
        if q_low > high or q_high < low:
            return math.inf

        # partial overlap
        mid = (low + high) // 2
        return min(
            self.search_st_array(q_low, q_high, low, mid, 2 * pos + 1),
            self.search_st_array(q_low, q_high, mid + 1, high, 2 * pos + 2),
        )


st = SegmentTree([-1, 0, 3, 6])
st.create_st_array(0, 3, 0)
print(st.st_array)

print(st.search_st_array(0, 3, 0, 3, 0))
