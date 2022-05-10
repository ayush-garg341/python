"""
Given an array of intervals, find the next interval of each interval. In a list of intervals,
for an interval i its next interval j will have the smallest ‘start’ greater than or equal to the ‘end’ of i.

example1:
    Input: Intervals [[2,3], [3,4], [5,6]]
    Output: [1, 2, -1]
    Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6]
        having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.
"""

import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    result = [None] * len(intervals)
    max_start_heap = []
    max_end_heap = []
    for i in range(len(intervals)):
        heapq.heappush(max_start_heap, (-intervals[i].start, i))
        heapq.heappush(max_end_heap, (-intervals[i].end, i))

    while max_end_heap:
        end = heapq.heappop(max_end_heap)
        top_end = -end[0]
        top_end_index = end[1]
        next_index = -1
        start = None
        while max_start_heap and top_end <= -max_start_heap[0][0]:
            start = heapq.heappop(max_start_heap)
            top_start_index = start[1]
            next_index = top_start_index
        if start:
            heapq.heappush(max_start_heap, start)
        result[top_end_index] = next_index

    return result


def main():

    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval([Interval(1, 1), Interval(3, 4)])
    print("Next interval indices are: " + str(result))


main()
