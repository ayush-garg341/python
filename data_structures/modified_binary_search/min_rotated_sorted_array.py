"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

example1:
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

example2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""

from typing import List


def findMin(arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid + 1]
        elif arr[mid] < arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    if start == len(arr) - 1:
        return arr[0]
    return arr[start + 1]


print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([11, 13, 15, 17]))
