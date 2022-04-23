"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates,
which means some numbers will be missing. Find all those missing numbers.

example1:
    Input: [2, 3, 1, 8, 2, 3, 5, 1]
    Output: 4, 6, 7
    Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

example2:
    Input: [2, 4, 1, 2]
    Output: 3
"""


def find_missing_numbers(nums):
    missingNumbers = []
    # TODO: Write your code here

    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != i + 1 and nums[j] != nums[i]:
            index = nums[i] - 1
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
    return missingNumbers


print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_missing_numbers([2, 4, 1, 2]))
print(find_missing_numbers([2, 3, 2, 1]))
