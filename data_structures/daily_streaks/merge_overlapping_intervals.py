"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
"""

def merge_intervals(intervals):
    intervals.sort(key = lambda x: x[0])
    new_intervals = []
    prev_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= prev_interval[1]:
            if intervals[i][1] > prev_interval[1]:
                prev_interval[1] = intervals[i][1]
        else:
            new_intervals.append(prev_interval)
            prev_interval = intervals[i]
    new_intervals.append(prev_interval)

    return new_intervals

print(merge_intervals([[6,7], [2,4], [5,9]]))
print(merge_intervals([[1,4], [2,6], [3,5]]))
print(merge_intervals([[1,4], [2,5], [7,9]]))
