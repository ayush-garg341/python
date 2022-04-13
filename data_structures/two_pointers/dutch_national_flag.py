"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
hence, we can’t count 0s, 1s, and 2s to recreate the array.

example1:
    Input: [1, 0, 2, 1, 0]
    Output: [0, 0, 1, 1, 2]

example2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0, 0, 1, 2, 2, 2,]
"""


def sort_with_extra_space(nums):
    nums_count = {}
    sorted_arr = []
    for num in nums:
        if num not in nums_count:
            nums_count[num] = 0
        nums_count[num] += 1

    zero_count = nums_count[0]
    one_count = nums_count[1]
    two_count = nums_count[2]
    for i in range(zero_count):
        sorted_arr.append(0)

    for i in range(one_count):
        sorted_arr.append(1)

    for i in range(two_count):
        sorted_arr.append(2)

    return sorted_arr


print(sort_with_extra_space([1, 0, 2, 1, 0]))
print(sort_with_extra_space([2, 2, 0, 1, 2, 0]))


def sort_in_place(nums):
    low = 0
    high = len(nums) - 1

    i = 0

    while i <= high:
        if nums[i] == 0:
            nums[low], nums[i] = nums[i], nums[low]
            i += 1
            low += 1

        elif nums[i] == 1:
            i += 1

        else:
            nums[high], nums[i] = nums[i], nums[high]
            high -= 1

    return nums


print(sort_in_place([1, 0, 2, 1, 0]))
print(sort_in_place([2, 2, 0, 1, 2, 0]))
