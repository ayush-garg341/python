"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position.
Merge all necessary intervals to produce a list that has only mutually exclusive intervals.
"""


def insert_interval(intervals, interval):
    idx = len(interval)
    for i in range(len(intervals)):
        if intervals[i][0] >= interval[0]:
            idx = i
            break

    intervals.insert(idx, interval)

    prev_interval = intervals[0]
    merge_intervals = []
    for i in range(1, len(intervals)):
        if prev_interval[1] >= intervals[i][0]:
            if intervals[i][1] > prev_interval[1]:
                prev_interval[1] = intervals[i][1]
        else:
            merge_intervals.append(prev_interval)
            prev_interval = intervals[i]

    merge_intervals.append(prev_interval)
    return merge_intervals


print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insert_interval([[2, 3], [5, 7]], [1, 4]))
