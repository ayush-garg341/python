"""
Given an array of nums, each num occurring twice except one.
Find the single number.
"""


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


print(single_number([1, 2, 2, 3, 3, 1, 4]))
print(single_number([2, 2, 1]))
