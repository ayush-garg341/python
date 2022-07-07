"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct
position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

example1:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
    Output: [[1,3], [4,7], [8,12]]
    Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

example2:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
    Output: [[1,3], [4,12]]
    Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

example3:
    Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
    Output: [[1,4], [5,7]]
    Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


def insert_interval(intervals, interval):
    merged_interval = []

    merged = False
    for i in range(len(intervals)):
        if intervals[i][0] < interval[0] and not merged:
            merged_interval.append(intervals[i])
        elif merged is True:
            merged_interval.append(intervals[i])
        else:
            merged_interval.append(interval)
            merged_interval.append(intervals[i])
            merged = True

    if merged is False:
        merged_interval.append(interval)

    merged = []
    first = merged_interval[0]
    for i in range(1, len(merged_interval)):
        if merged_interval[i][0] <= first[1]:
            if merged_interval[i][1] > first[1]:
                first[1] = merged_interval[i][1]
        else:
            merged.append(first)
            first = merged_interval[i]
    merged.append(first)

    return merged


print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insert_interval([[2, 3], [5, 7]], [1, 4]))
print(insert_interval([[1, 5]], [5, 7]))


def insert_interval_without_extra_space(intervals, interval):
    merged_interval = []

    # finding the position to insert new interval
    merged = False
    for i in range(len(intervals)):
        if intervals[i][0] < interval[0] and not merged:
            merged_interval.append(intervals[i])
        elif merged is True:
            merged_interval.append(intervals[i])
        else:
            merged_interval.append(interval)
            merged_interval.append(intervals[i])
            merged = True

    if merged is False:
        merged_interval.append(interval)

    # now merging the intervals in place to make them mutually exclusive
    start = 0
    first = merged_interval[0]
    for i in range(1, len(merged_interval)):
        if merged_interval[i][0] <= first[1]:
            if merged_interval[i][1] > first[1]:
                first[1] = merged_interval[i][1]
        else:
            merged_interval[start] = first
            start += 1
            first = merged_interval[i]
    merged_interval[start] = first

    return merged_interval[: start + 1]


print(" ================ ")
print(insert_interval_without_extra_space([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(insert_interval_without_extra_space([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insert_interval_without_extra_space([[2, 3], [5, 7]], [1, 4]))
print(insert_interval_without_extra_space([[1, 5]], [5, 7]))


def insert_interval_test(intervals, interval):
    merged_interval = []
    start_range = interval[0]
    pos = len(intervals)
    for i in range(len(intervals)):
        if intervals[i][0] <= start_range:
            continue
        else:
            pos = i
            break
    intervals.insert(pos, interval)

    start_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= start_interval[1]:
            if intervals[i][1] > start_interval[1]:
                start_interval[1] = intervals[i][1]

        else:
            merged_interval.append(start_interval)
            start_interval = intervals[i]

    merged_interval.append(start_interval)
    return merged_interval


print("===============")

print(insert_interval_test([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(insert_interval_test([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insert_interval_test([[2, 3], [5, 7]], [1, 4]))
print(insert_interval_test([[1, 5]], [5, 7]))
