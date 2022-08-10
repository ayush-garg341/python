"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

example1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

example2:
    Input: nums = [2,3,0,1,4]
    Output: 2
"""
import math


def min_jump(nums):
    return min_jump_rec(nums, 0)


def min_jump_rec(nums, i):
    if i >= len(nums) - 1:
        return 0
    current_jump = nums[i]
    min_jumps = math.inf
    jump = 1
    while jump <= current_jump:
        index = i + jump
        if index < len(nums):
            min_jumps = min(min_jumps, 1 + min_jump_rec(nums, index))

        jump += 1

    return min_jumps

print(min_jump([2,3,1,1,4]))
print(min_jump([2,3,0,1,4]))


def min_jump_top_down(nums):
    dp = [0 for i in range(len(nums))]
    return min_jump_top_down_dp(nums, 0, dp)


def min_jump_top_down_dp(nums, i, dp):
    """
    TC -> O(n^2)
    """
    if i >= len(nums) - 1:
        return 0
    if dp[i]:
        return dp[i]
    current_jump = nums[i]
    min_jumps = math.inf
    jump = 1
    while jump <= current_jump:
        index = i + jump
        min_jumps = min(min_jumps, 1+min_jump_top_down_dp(nums, index, dp))
        jump += 1

    dp[i] = min_jumps
    return dp[i]

print("========= top down memoization ============")
print(min_jump_top_down([2,3,1,1,4]))
print(min_jump_top_down([2,3,0,1,4]))


def min_jump_dp_bottom_up(nums):
    """
    TC -> O(n^2)
    """
    n = len(nums)
    min_jump_to_reach_end = [math.inf for i in range(n)]
    min_jump_to_reach_end[n-1] = 0
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            max_jump = i + nums[i]
            if max_jump >= j:
                min_jump_to_reach_end[i] = min(min_jump_to_reach_end[i], 1+min_jump_to_reach_end[j])

    return min_jump_to_reach_end[0]
print("============ bottom up =================")
print(min_jump_dp_bottom_up([2,3,1,1,4]))
print(min_jump_dp_bottom_up([2,3,0,1,4]))


def min_jump_to_reach_end_greedy(nums):
    """
    TC -> O(n)
    Greedy and uses BFS approach
    """

    min_jump = 0
    l, r = 0, 0

    while r < len(nums) - 1:
        farthest = 0

        for i in range(l, r+1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest

        min_jump += 1

    return min_jump

print(" ================ greedy appraoch BFS ================")

print(min_jump_to_reach_end_greedy([3,3,1,1,4]))
print(min_jump_to_reach_end_greedy([2,3,0,1,4]))

