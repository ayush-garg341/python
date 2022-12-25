"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing
the duplicates in-place return the length of the subarray that has no duplicate in it.

example1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

example2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


def remove_duplicates(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    next_num = 0

    for next_non_dup in range(1, len(arr)):
        if arr[next_non_dup] == arr[next_num]:
            next_non_dup += 1
        else:
            next_num += 1
            arr[next_num] = arr[next_non_dup]

    return arr[0 : next_num + 1]


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))


def remove_duplicates_simpler(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    start = 0
    for i in range(1, len(arr)):
        if arr[start] != arr[i]:
            arr[start + 1] = arr[i]
            start += 1

    return arr[: start + 1]


print(remove_duplicates_simpler([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates_simpler([2, 2, 2, 11]))
