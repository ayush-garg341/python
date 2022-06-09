"""
Given an array nums, return true if the array was originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

example1:
    Input: nums = [3,4,5,1,2]
    Output: true
    Explanation: [1,2,3,4,5] is the original sorted array.
    You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

example2:
    Input: nums = [2,1,3,4]
    Output: false
    Explanation: There is no sorted array once rotated that can make nums.

example3:
    Input: nums = [1,2,3]
    Output: true
    Explanation: [1,2,3] is the original sorted array.
    You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""

from typing import List


def check(nums: List[int]) -> bool:
    found = False
    for i in range(len(nums)):
        found = check_if_sorted_from_current_pos(i, nums)
        if found:
            return True
    return False


def check_if_sorted_from_current_pos(pos, nums):
    n = len(nums)
    i = 0
    while i < n - 1:
        if nums[(pos + 1) % n] < nums[pos % n]:
            return False
        pos += 1
        i += 1
    return True


print(check([3, 4, 5, 1, 2]))
print(check([2, 1, 3, 4]))
print(check([1, 2, 3]))
