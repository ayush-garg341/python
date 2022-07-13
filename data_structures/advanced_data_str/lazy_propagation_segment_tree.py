"""
Create lazy propagation segment tree for frequent updates.
"""

import math


class LazyUpdatesSegmentTree:
    def __init__(self, array):
        self._array = array
        self._size = len(self._array)
        self._st_size = 2 * self._size - 1
        self._segment_tree_array = [0 for i in range(self._st_size)]
        self._lazy_tree = [0 for i in range(self._st_size)]

    def create_segment_tree(self, low, high, pos):
        if low == high:
            self._segment_tree_array[pos] = self._array[low]
            return

        mid = (low + high) // 2

        self.create_segment_tree(low, mid, 2 * pos + 1)
        self.create_segment_tree(mid + 1, high, 2 * pos + 2)

        self._segment_tree_array[pos] = min(
            self._segment_tree_array[2 * pos + 1], self._segment_tree_array[2 * pos + 2]
        )

    def update_lazy_segment_tree(self, q_low, q_high, low, high, pos, delta):
        if high < low:
            return

        # if pos at lazy tree is not 0, it means we have previous update to apply in segemnt tree
        if self._lazy_tree[pos] != 0:
            self._segment_tree_array[pos] += self._lazy_tree[pos]
            if low != high:
                self._lazy_tree[2 * pos + 1] += self._lazy_tree[pos]
                self._lazy_tree[2 * pos + 2] += self._lazy_tree[pos]

            self._lazy_tree[pos] = 0

        # No overlap
        if q_low > high or q_high < low:
            return

        # complete overlap
        # Incrementing bu delta
        # No need to update below subtrees as it will lead to increasing time complexitty
        if q_low <= low and q_high >= high:
            self._segment_tree_array[pos] += delta
            if low != high:
                self._lazy_tree[2 * pos + 1] += delta
                self._lazy_tree[2 * pos + 2] += delta

            return

        mid = (low + high) // 2
        self.update_lazy_segment_tree(q_low, q_high, low, mid, 2 * pos + 1, delta)
        self.update_lazy_segment_tree(q_low, q_high, mid + 1, high, 2 * pos + 2, delta)
        self._segment_tree_array[pos] = min(
            self._segment_tree_array[2 * pos + 1], self._segment_tree_array[2 * pos + 2]
        )

    def search_lazy_segment_tree(self, q_low, q_high, low, high, pos):
        if high < low:
            return math.inf
        if self._lazy_tree[pos] != 0:
            self._segment_tree_array[pos] += self._lazy_tree[pos]
            if low != high:
                self._lazy_tree[2 * pos + 1] = self._lazy_tree[pos]
                self._lazy_tree[2 * pos + 2] = self._lazy_tree[pos]
            self._lazy_tree[pos] = 0

        # No overlap
        if q_low > high or q_high < low:
            return math.inf

        # complete overlap
        if q_low <= low and q_high >= high:
            return self._segment_tree_array[pos]

        mid = (low + high) // 2
        return min(
            self.search_lazy_segment_tree(q_low, q_high, low, mid, 2 * pos + 1),
            self.search_lazy_segment_tree(q_low, q_high, mid + 1, high, 2 * pos + 2),
        )


st = LazyUpdatesSegmentTree([-1, 2, 4, 1, 7, 1, 3, 2])
# creating segment array
st.create_segment_tree(0, 7, 0)
# printing that segment array
print(st._segment_tree_array)

# searching in range 4-7 in original array
print(st.search_lazy_segment_tree(4, 7, 0, 7, 0))

# searching in range 0-3 in original array
print(st.search_lazy_segment_tree(0, 3, 0, 7, 0))

# update the interval in original array from 0-3 by 3
st.update_lazy_segment_tree(0, 3, 0, 7, 0, 3)
print(st._segment_tree_array)

# searching after updating interval 0-3
print(st.search_lazy_segment_tree(0, 3, 0, 7, 0))

# update in range 0-3 by 1
st.update_lazy_segment_tree(0, 3, 0, 7, 0, 1)
print(st._segment_tree_array)
print(st.search_lazy_segment_tree(0, 3, 0, 7, 0))

# update in range 0-0 by 2
st.update_lazy_segment_tree(0, 0, 0, 7, 0, 2)
print(st._segment_tree_array)
print(st.search_lazy_segment_tree(3, 5, 0, 7, 0))
