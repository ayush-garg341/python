"""
In Selection sort we select minimum, and put (swap) that at beginning of the array.
This way left part is sorted and right part is un-sorted.
"""


def selection_sort(nums):
    pos = 0
    for i in range(len(nums)):
        mim = nums[i]
        index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < mim:
                mim = nums[j]
                index = j
        nums[pos], nums[index] = nums[index], nums[pos]
        pos += 1

    return nums


nums = [5, 4, 1, 3, 2]
print(selection_sort(nums))

nums = [-1, -2, -3, -5, -4]
print(selection_sort(nums))
