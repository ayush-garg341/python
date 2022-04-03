"""
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’

example1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

example2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
"""

import math


def smallest_sub_arr_greater_sum(arr: list, s: int) -> float:
    length = math.inf
    sum_k = 0
    window_start = 0
    for window_end in range(len(arr)):
        sum_k += arr[window_end]

        while sum_k >= s:
            length = min(length, window_end - window_start + 1)
            sum_k -= arr[window_start]
            window_start += 1
    return length if length != math.inf else 0


print(smallest_sub_arr_greater_sum([2, 1, 5, 2, 3, 2], 7))
print(smallest_sub_arr_greater_sum([2, 1, 5, 2, 8], 7))
print(smallest_sub_arr_greater_sum([3, 4, 1, 1, 6], 8))
