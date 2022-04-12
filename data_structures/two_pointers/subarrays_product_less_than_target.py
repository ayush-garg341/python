"""
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays
whose product is less than the target number.

example1:
    Input: [2, 5, 3, 10], target=30
    Output: [2], [5], [2, 5], [3], [5, 3], [10]
    Explanation: There are six contiguous subarrays whose product is less than the target.

example2:
    Input: [8, 2, 6, 5], target=50
    Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
    Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

from collections import deque


def find_subarrays(arr, target):
    results = []
    window_start = 0
    product = 1
    count = 0
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        product *= right_char

        while product >= target and window_start < len(arr):
            product = product / arr[window_start]
            window_start += 1

        if window_end - window_start >= 0:
            count += window_end - window_start + 1

        temp_list = deque()
        for i in range(window_end, window_start - 1, -1):
            temp_list.appendleft(arr[i])
            results.append(list(temp_list))

    print("count == ", count)

    return results


print(find_subarrays([2, 5, 3, 10], 30))
print(find_subarrays([8, 2, 6, 5], 50))
print(find_subarrays([5, 10, 2], 10))
