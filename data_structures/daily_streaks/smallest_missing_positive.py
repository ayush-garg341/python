"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.
"""
from typing import List
def firstMissingPositive(nums: List[int]) -> int:
    zero_exists = False
    for num in nums:
        if num == 0:
            zero_exists = True
            break
    if not zero_exists:
        i = 0
        while i < len(nums):
            if nums[i] != i+1 and nums[i] > 0 and nums[i] < len(nums) and nums[i]!=nums[nums[i]-1]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
    else:
        i = 0
        while i < len(nums):
            if nums[i] != i and nums[i] >= 0 and nums[i] < len(nums) and nums[i]!=nums[nums[i]]:
                idx = nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


print(firstMissingPositive([-3, 1, 5, 4, 2]))
print(firstMissingPositive([3, -2, 0, 1, 2]))
print(firstMissingPositive([3, 2, 5, 1]))
