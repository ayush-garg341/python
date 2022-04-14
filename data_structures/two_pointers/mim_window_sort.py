"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

example1:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

example2:
    Input: [1, 3, 2, 0, -1, 7, 10]
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
"""


def shortest_window_short_naive(arr):
    nums = []
    for num in arr:
        nums.append(num)
    arr.sort()
    start = -1
    for i in range(len(arr)):
        if arr[i] == nums[i]:
            continue
        else:
            start = i
            break

    end = len(arr)
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == nums[i]:
            continue
        else:
            end = i
            break

    if end == len(arr) and start == -1:
        return 0
    return end - start + 1


print(shortest_window_short_naive([1, 2, 5, 3, 7, 10, 9, 12]))
print(shortest_window_short_naive([1, 3, 2, 0, -1, 7, 10]))
print(shortest_window_short_naive([1, 2, 3]))
print(shortest_window_short_naive([3, 2, 1]))

import math


def mim_window_sort(arr):
    n = len(arr)
    mim_num = math.inf
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            mim_num = min(mim_num, arr[i])

    max_num = -math.inf
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            max_num = max(max_num, arr[i])

    low = 0
    for i in range(n):
        if arr[i] > mim_num:
            low = i
            break

    high = n - 1
    for i in range(n - 1, -1, -1):
        if arr[i] < max_num:
            high = i
            break

    if mim_num == math.inf and max_num == -math.inf:
        return 0

    return high - low + 1


print(" ======================== ")
print(mim_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(mim_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(mim_window_sort([1, 2, 3]))
print(mim_window_sort([3, 2, 1]))
