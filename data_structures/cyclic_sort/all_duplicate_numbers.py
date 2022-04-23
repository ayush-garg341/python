"""
We are given an unsorted array containing n numbers taken from the range 1 to n.
The array has some numbers appearing twice, find all these duplicate numbers using constant space.

example1:
    Input: [3, 4, 4, 5, 5]
    Output: [4, 5]

example2:
    Input: [5, 4, 7, 2, 3, 5, 3]
    Output: [3, 5]
"""


def find_all_duplicates(nums):
    duplicateNumbers = []
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])
    return duplicateNumbers


print(find_all_duplicates([3, 4, 4, 5, 5]))
print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
