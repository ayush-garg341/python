"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

example1:
    Input: [ [1,2], [2,3], [3,4], [1,3] ]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

example2:
    Input: [ [1,2], [1,2], [1,2] ]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_number_intervals(intervals):
    intervals.sort(key=lambda x: x.start)
    prev = intervals[0]

    remove_count = 0
    for i in range(1, len(intervals)):
        current = intervals[i]
        if current.start < prev.end:
            remove_count += 1
            if prev.end > current.end:
                prev = current
        else:
            prev = current

    return remove_count


print(min_number_intervals([Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1, 3)]))
print(min_number_intervals([Interval(1, 2), Interval(1, 2), Interval(1, 2)]))
