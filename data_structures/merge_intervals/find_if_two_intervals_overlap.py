"""
Given a set of intervals, find out if any two intervals overlap.

example1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: true
    Explanation: Intervals [1,4] and [2,5] overlap
"""


def check_two_intervals_overlap(intervals):
    if len(intervals) < 2:
        return False
    intervals.sort()
    first_elt = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= first_elt[1]:
            return True
        else:
            first_elt = intervals[i]

    return False


print(check_two_intervals_overlap([[1, 4], [2, 5], [7, 9]]))
