"""
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be
greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.

example1:
Input:
    [-2,2,-3,4,-1,2,1,-5,3]
    5

output:
    5

explanation:
    [2,-3,4,-1,2,1]
    sum = 5

"""


import math


def max_subarray(nums, k):
    if k <= 0 or len(nums) < k:
        return 0
    # kadane's algo
    best_sum_at_every_index = [None] * len(nums)

    best_sum_at_every_index[0] = nums[0]
    local_sum = nums[0]
    for i in range(1, len(nums)):
        if local_sum + nums[i] >= nums[i]:
            local_sum = local_sum + nums[i]
        else:
            local_sum = nums[i]
        best_sum_at_every_index[i] = local_sum

    print(best_sum_at_every_index)

    # k window sum
    overall_max = -math.inf
    exact_k = 0
    for i in range(0, k):
        exact_k += nums[i]
    if exact_k > overall_max:
        overall_max = exact_k

    for i in range(k, len(nums)):
        exact_k += nums[i] - nums[i - k]
        if exact_k > overall_max:
            overall_max = exact_k
        more_than_k = exact_k + best_sum_at_every_index[i - k]
        if more_than_k > overall_max:
            overall_max = more_than_k

    return overall_max


print(max_subarray([-2, 2, -3, 4, -1, 2, 1, -5, 3], 5))
print(max_subarray([5, -10, 4], 2))
print(max_subarray([-5, 15], 1))
print(max_subarray([-1, -1, -1, -1], 2))
