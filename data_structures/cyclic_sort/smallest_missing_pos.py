"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.
Note: Positive numbers start from ‘1’.

example1:
    Input: [-3, 1, 5, 4, 2]
    Output: 3
    Explanation: The smallest missing positive number is '3'

example2:
    Input: [3, -2, 0, 1, 2]
    Output: 4

example3:
    Input: [3, 2, 5, 1]
    Output: 4
"""


def find_first_smallest_missing_positive(nums):
    # TODO: Write your code here
    # return find_first_smallest_missing_positive_extra_space(nums)
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1


def find_first_smallest_missing_positive_extra_space(nums):
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 0
        num_dict[num] += 1

    n = len(nums)
    for i in range(1, n + 2):
        if i not in num_dict:
            return i


print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
print(find_first_smallest_missing_positive([3, 2, 5, 1]))
print(find_first_smallest_missing_positive([1]))
print(find_first_smallest_missing_positive([2, 1]))
print(find_first_smallest_missing_positive([-1, 4, 2, 1, 9, 10]))
print(find_first_smallest_missing_positive([2, 2, 4, 0, 1, 3, 3, 3, 4, 3]))
