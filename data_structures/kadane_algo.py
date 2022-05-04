"""
Given an array of integers, find a contiguous subarray which has the largest sum.
"""

import math


def kadane_algo(nums):
    overall_sum = nums[0]
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


def max_subarray_sum_divide_and_conquer(nums):
    max_sum = max_subarray_sum_divide_and_conquer_rec(nums, 0, len(nums) - 1)
    return max_sum


def max_subarray_sum_divide_and_conquer_rec(nums, p, r):
    if p == r:
        return nums[p]
    q = (p + r) // 2

    left_max = max_subarray_sum_divide_and_conquer_rec(nums, p, q)
    right_max = max_subarray_sum_divide_and_conquer_rec(nums, q + 1, r)
    crossing_max = max_subarray_crossing_sum(nums, p, q, r)

    return max(max(left_max, right_max), crossing_max)


def max_subarray_crossing_sum(nums, p, q, r):
    left_sum = -math.inf
    local_sum = 0
    for i in range(q, p - 1, -1):
        local_sum += nums[i]
        if local_sum > left_sum:
            left_sum = local_sum

    right_sum = -math.inf
    local_sum = 0
    for i in range(q + 1, r + 1):
        local_sum += nums[i]
        if local_sum > right_sum:
            right_sum = local_sum

    return left_sum + right_sum


print(max_subarray_sum_divide_and_conquer([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
print(max_subarray_sum_divide_and_conquer([1, 2, 3, 4]))
