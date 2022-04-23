"""
We are given an array containing n objects. Each object, when created, was assigned a unique number
from the range 1 to n based on their creation sequence.
Write a function to sort the objects in-place on their creation sequence number in O(n)
O(n) and without using any extra space.

example1:
    Input: [3, 1, 5, 4, 2]
    Output: [1, 2, 3, 4, 5]

example2:
    Input: [2, 6, 4, 3, 1, 5]
    Output: [1, 2, 3, 4, 5, 6]
"""


def cyclic_sort(nums):
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] != i + 1:
            index = nums[i] - 1
            nums[i], nums[index] = nums[index], nums[i]
            # temp = nums[index]
            # nums[index] = nums[i]
            # nums[i] = temp
        else:
            i += 1
    return nums


print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))
