"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the
longest contiguous subarray having all 1s.

example1:
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

example2:
    Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
    Output: 9
    Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def longest_ones_subarray_replacement(array: list, k: int):
    window_start = 0
    max_len = 0

    distinct = {}
    distinct[0] = 0
    distinct[1] = 0
    for window_end in range(len(array)):
        num = array[window_end]
        distinct[num] += 1

        while distinct[0] > k:
            left_num = array[window_start]
            distinct[left_num] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    return max_len


print(longest_ones_subarray_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longest_ones_subarray_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
