"""
We assume that there are two list sorted and unsorted ( 0th element is always sorted )
And now iterating over unsorted list we keep the element at correct position in sorted list.
"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        hole = i
        current_val = nums[i]
        while hole > 0 and nums[hole - 1] > current_val:
            nums[hole] = nums[hole - 1]
            hole = hole - 1
        nums[hole] = current_val

    return nums


nums = [5, 4, 1, 3, 2, 6]
print(insertion_sort(nums))

nums = [-1, -2, -3, -5, -4]
print(insertion_sort(nums))
