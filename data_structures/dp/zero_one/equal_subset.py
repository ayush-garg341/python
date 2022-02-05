"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
"""


def can_partition(nums: list) -> bool:
    """
    params: list of nums
    return: bool (True/False)
    """
    can = False
    current_idx = 0
    s = sum(nums)
    if s%2 != 0:
        return False

    can = can_partition_recursive(nums, current_idx, s/2)
    return can

def can_partition_recursive(nums: list, current_idx: int, s: float) -> bool:

    """
        params:
            nums:- list of nums
            current_idx: current index of list
            s:- s is the sum we are looking for
        return: bool(True/False)
    """
    if s == 0:
        return True

    if current_idx >= len(nums):
        return False

    if nums[current_idx] <= s:
        if can_partition_recursive(nums, current_idx+1, s-nums[current_idx]):
            return True

    return can_partition_recursive(nums, current_idx+1, s)


can = can_partition([1, 2, 3, 4])
print(can)


can = can_partition([1, 1, 3, 4, 7])
print(can)

can = can_partition([2, 3, 4, 6])
print(can)


def can_partition_recursive_top_bottom(nums: list) -> bool:
    can = False
    current_idx = 0
    s = sum(nums)
    if s%2 != 0:
        return False

    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(nums))]
    can = can_partition_recursive_with_memoization(nums, current_idx, dp, s/2)
    if can == 1:
        return True
    return False

def can_partition_recursive_with_memoization(nums: list, current_idx: int, dp:list, s: float) -> int:

    """
        params:
            nums:- list of nums
            current_idx: current index of list
            dp: list of lists to memoize/store results
            s:- s is the sum we are looking for
        return: bool(True/False)
    """

    if s == 0:
        return 1

    if current_idx >= len(nums):
        return 0

    if dp[current_idx][s] == -1:
        if nums[current_idx] <= s:
            if can_partition_recursive_with_memoization(nums, current_idx+1, dp, s-nums[current_idx]):
                dp[current_idx][s] = 1
                return 1

        dp[current_idx][s] = can_partition_recursive_with_memoization(nums, current_idx+1, dp, s)
    return dp[current_idx][s]

can = can_partition([1, 2, 3, 4])
print(can)


can = can_partition([1, 1, 3, 4, 7])
print(can)

can = can_partition([2, 3, 4, 6])
print(can)


def can_partition_bottoms_up(nums) -> bool:
    """
    params:
        nums: list of nums
    return:
        bool: true/false
    """

    n = len(nums)
    if n<=0:
        return False

    s = sum(nums)
    if s%2 !=0:
        return False

    dp = [[-1 for i in range(int(s/2)+1)] for j in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1

    for i in range(int(s/2)+1):
        if nums[0]<= s/2:
            dp[0][i] = 1

    for i in range(1, len(nums)):
        for s in range(int(s/2)+1):
            if dp[i-1][s]==1:
                dp[i][s] = 1
            elif nums[i] <= s:
                dp[i][s] = dp[i-1][nums[i]-s]

    if dp[len(nums)-1][int(s/2)] == 1:
        return True
    return False

can = can_partition_bottoms_up([1, 2, 3, 4])
print(can)


can = can_partition_bottoms_up([1, 1, 3, 4, 7])
print(can)

can = can_partition_bottoms_up([2, 3, 4, 6])
print(can)

