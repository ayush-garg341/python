"""
You are given an array of intervals, where intervals[i] = [starti, endi] and
each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi
and startj is minimized. Note that i may equal j
"""

import heapq
from typing import List


def findRightInterval(intervals: List[List[int]]) -> List[int]:
    min_end_heap = []
    min_start_heap = []

    result = []
    for i in range(len(intervals)):
        heapq.heappush(min_end_heap, (intervals[i][1], i))
        heapq.heappush(min_start_heap, (intervals[i][0], i))
        result.append(-1)

    while min_end_heap and min_start_heap:
        if min_end_heap[0][0] <= min_start_heap[0][0]:
            val, idx = heapq.heappop(min_end_heap)
            right_idx = min_start_heap[0][1]
            result[idx] = right_idx
        else:
            heapq.heappop(min_start_heap)

    return result


print(findRightInterval([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]))
