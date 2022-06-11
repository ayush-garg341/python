"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

example1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

example2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

example3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
"""

from typing import List
import math


def minSubArrayLen(target: int, nums: List[int]) -> float:
    window_start = 0
    current_sum = 0
    min_len = math.inf
    for window_end in range(len(nums)):
        current_sum += nums[window_end]
        while window_start <= window_end and current_sum >= target:
            if current_sum >= target:
                min_len = min(min_len, window_end - window_start + 1)

            current_sum -= nums[window_start]
            window_start += 1
    return min_len if min_len != math.inf else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
