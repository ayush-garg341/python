"""
Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.

ex1:
    input - arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    output - [2, 3], [5, 6], [7, 7]

ex2:
    input - arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    output - [5, 7], [9, 10]
"""

def merge(intervals_a, intervals_b):
    result = []
    # TODO: Write your code here
    i = 0
    j = 0
    temp_interval = [None]*2
    while i < len(intervals_a) and j < len(intervals_b):
        if ( intervals_b[j][0] >= intervals_a[i][0] and intervals_b[j][0] <= intervals_a[i][1] ) or (intervals_a[i][0] >= intervals_b[j][0] and intervals_a[i][0] <= intervals_b[j][1]):
            temp_interval[0] = max(intervals_a[i][0], intervals_b[j][0])
            temp_interval[1] = min(intervals_a[i][1], intervals_b[j][1])
            result.append(temp_interval)
            temp_interval = [None]*2
            if intervals_b[j][1] > intervals_a[i][1]:
                i += 1
            else:
                j += 1

        elif ( intervals_b[j][1] >= intervals_a[i][0] and intervals_b[j][1] <= intervals_a[i][1] ) or (intervals_a[i][1] >= intervals_b[j][0] and intervals_a[i][1] <= intervals_b[j][1]):
            temp_interval[0] = max(intervals_a[i][0], intervals_b[j][0])
            temp_interval[1] = min(intervals_a[i][1], intervals_b[j][1])
            result.append(temp_interval)
            temp_interval = [None] * 2
            if intervals_b[j][1] < intervals_a[i][1]:
                j += 1
            else:
                i += 1

        elif intervals_b[j][1] < intervals_a[i][0]:
            j += 1
        else:
            i += 1
    return result

print(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 9]]))
print(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
print(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 9]]))
