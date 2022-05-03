"""
Given an array of integers, find a contiguous subarray which has the largest sum.
"""
import math


def kadane_algo(nums):
    overall_sum = -math.inf
    s = nums[0]
    for i in range(1, len(nums)):
        if s + nums[i] >= nums[i]:
            s += nums[i]
        else:
            s = nums[i]
        overall_sum = max(overall_sum, s)

    return overall_sum


print(kadane_algo([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
print(kadane_algo([1, 2, 3, 4]))
