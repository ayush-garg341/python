"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of
disjoint intervals sorted on their start time.

example1:
    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]
    Explanation: The output list contains the common intervals between the two lists.

example2:
    Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    Output: [5, 7], [9, 10]
    Explanation: The output list contains the common intervals between the two lists.
"""


def merge(intervals_b, intervals_a):
    j = 0
    i = 0
    len_a = len(intervals_a)
    len_b = len(intervals_b)

    merged = []
    while i < len_a and j < len_b:

        # a and b do not overlap
        if intervals_a[i][1] < intervals_b[j][0]:
            i += 1
        # b and a do not overlap
        elif intervals_a[i][0] > intervals_b[j][1]:
            j += 1
        # b overlaps a and a ends after b
        elif (
            intervals_a[i][0] <= intervals_b[j][1]
            and intervals_a[i][1] > intervals_b[j][1]
        ):
            min_a = max(intervals_a[i][0], intervals_b[j][0])
            min_b = intervals_b[j][1]
            merged.append([min_a, min_b])
            j += 1
        # a overlaps b and b ends after a
        elif (
            intervals_a[i][1] >= intervals_b[j][0]
            and intervals_a[i][0] < intervals_b[j][0]
        ):
            min_a = intervals_b[j][0]
            min_b = min(intervals_a[i][1], intervals_b[j][1])
            merged.append([min_a, min_b])
            i += 1
        # b completely overlaps a
        elif (
            intervals_a[i][0] >= intervals_b[j][0]
            and intervals_a[i][1] <= intervals_b[j][1]
        ):
            min_a = max(intervals_a[i][0], intervals_b[j][0])
            min_b = min(intervals_a[i][1], intervals_b[j][1])
            merged.append([min_a, min_b])
            if intervals_a[i][1] == intervals_b[j][1]:
                i += 1
                j += 1
            else:
                i += 1
        # a completely overlap b
        elif (
            intervals_a[i][0] <= intervals_b[j][0]
            and intervals_a[1][1] >= intervals_b[j][1]
        ):
            min_a = max(intervals_a[i][0], intervals_b[j][0])
            min_b = min(intervals_a[i][1], intervals_b[j][1])
            merged.append([min_a, min_b])
            if intervals_a[i][1] == intervals_b[j][1]:
                i += 1
                j += 1
            else:
                j += 1

    return merged


print(
    "Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
)
print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
