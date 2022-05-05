"""
Bubble sort pushes the largest element at the end of the array by swapping its position and shifting it to the end.
Right part will be the sorted part and left part will be un-sorted.
"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):  # Here it will be n -1 for 0th pass.
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


nums = [5, 4, 1, 3, 2, 6]
print(bubble_sort(nums))

nums = [-1, -2, -3, -5, -4]
print(bubble_sort(nums))
