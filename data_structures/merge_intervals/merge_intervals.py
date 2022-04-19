"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually
exclusive intervals.

example1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
    one [1,5].

example2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

"""


def merge_intervals(intervals):
    if len(intervals) == 1 or len(intervals) == 0:
        return intervals
    merged_interval_list = []
    intervals.sort()
    # intervals.sort(key=lambda x: x.start)
    first_list = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= first_list[1]:
            if intervals[i][1] > first_list[1]:
                first_list[1] = intervals[i][1]
        else:
            merged_interval_list.append(first_list)
            first_list = intervals[i]
    merged_interval_list.append(first_list)

    return merged_interval_list


print(merge_intervals([[1, 4], [2, 5], [7, 9]]))
print(merge_intervals([[6, 7], [2, 4], [5, 9]]))
print(merge_intervals([[1, 4], [2, 6], [3, 5]]))
