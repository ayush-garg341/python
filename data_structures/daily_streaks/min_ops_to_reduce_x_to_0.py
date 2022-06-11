"""
You are given an integer array nums and an integer x. In one operation,
you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.

Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

example1:
    Input: nums = [1,1,4,2,3], x = 5
    Output: 2
    Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

example2:
    Input: nums = [5,6,7,8,9], x = 4
    Output: -1

example3:
    Input: nums = [3,2,20,1,1,3], x = 10
    Output: 5
    Explanation: The optimal solution is to remove the last three elements and the first two elements
                (5 operations in total) to reduce x to zero.

"""

from typing import List


def minOperationsWrong(nums: List[int], x: int) -> int:
    n = len(nums)
    start = 0
    end = n - 1
    ops_count = 0
    while x != 0:
        if len(nums) == 0:
            return -1
        if nums[start] > nums[end] and nums[start] <= x:
            x = x - nums[start]
            nums.pop(start)
            ops_count += 1
            end -= 1
        elif nums[end] > nums[start] and nums[end] <= x:
            x = x - nums[end]
            nums.pop(end)
            ops_count += 1
            end -= 1
        elif nums[end] <= x:
            x = x - nums[end]
            nums.pop(end)
            ops_count += 1
            end -= 1
        elif nums[start] <= x:
            x = x - nums[start]
            nums.pop(start)
            ops_count += 1
            end -= 1
        else:
            return -1

    return ops_count


# print(minOperationsWrong([1, 1, 4, 2, 3], 5))
# print(minOperationsWrong([5, 6, 7, 8, 9], 4))
# print(minOperationsWrong([3, 2, 20, 1, 1, 3], 10))
# print(minOperationsWrong([1, 1], 3))
# print(
# minOperationsWrong(
# [
# 6016,
# 5483,
# 541,
# 4325,
# 8149,
# 3515,
# 7865,
# 2209,
# 9623,
# 9763,
# 4052,
# 6540,
# 2123,
# 2074,
# 765,
# 7520,
# 4941,
# 5290,
# 5868,
# 6150,
# 6006,
# 6077,
# 2856,
# 7826,
# 9119,
# ],
# 31841,
# )
# )


def min_ops_correct(nums: List[int], x: int) -> int:
    n = len(nums)
    total_sum = 0
    for num in nums:
        total_sum += num
    if total_sum == x:
        return n
    target = total_sum - x
    window_start = 0
    current_sum = 0
    max_len = 0
    for window_end in range(n):
        current_sum += nums[window_end]
        while window_start < window_end and current_sum > target:
            current_sum -= nums[window_start]
            window_start += 1
        if current_sum == target:
            max_len = max(max_len, window_end - window_start + 1)
    return n - max_len if max_len else -1


print(min_ops_correct([1, 1, 4, 2, 3], 5))
print(min_ops_correct([5, 6, 7, 8, 9], 4))
print(min_ops_correct([3, 2, 20, 1, 1, 3], 10))
print(min_ops_correct([1, 1], 3))
print(
    min_ops_correct(
        [
            6016,
            5483,
            541,
            4325,
            8149,
            3515,
            7865,
            2209,
            9623,
            9763,
            4052,
            6540,
            2123,
            2074,
            765,
            7520,
            4941,
            5290,
            5868,
            6150,
            6006,
            6077,
            2856,
            7826,
            9119,
        ],
        31841,
    )
)
