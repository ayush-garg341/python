"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.
Return the single element that appears only once.

example1:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

example2:
    Input: nums = [3,3,7,7,10,11,11]
    Output: 10
"""

from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    start = 0
    n = len(nums)
    end = n - 1

    while start < end:
        mid = (start + end) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif nums[mid] == nums[mid + 1]:
            len_elts = n - mid
            if len_elts % 2 == 0:
                end = mid - 1
            else:
                start = mid + 2
        elif nums[mid] == nums[mid - 1]:
            len_elts = mid + 1
            if len_elts % 2 == 0:
                start = mid + 1
            else:
                end = mid - 2
    return nums[start]


print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
