"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

example1:
    Input: [3, -1, 4, 5, 5], k=3
    Output: [1, 2, 6]
    Explanation: The smallest missing positive numbers are 1, 2 and 6.

example2:
    Input: [2, 3, 4], k=3
    Output: [1, 5, 6]
    Explanation: The smallest missing positive numbers are 1, 5 and 6.
"""


def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    # TODO: Write your code here

    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    count = 0
    pos_num = {}
    for i in range(n):
        if nums[i] > 0:
            pos_num[nums[i]] = 1
        if i + 1 != nums[i]:
            if count != k:
                missingNumbers.append(i + 1)
                count += 1
            else:
                break
    j = n + 1
    while count != k:
        if j not in pos_num:
            missingNumbers.append(j)
            count += 1
        j += 1
    return missingNumbers


print(find_first_k_missing_positive([3, -1, 4, 5, 5], k=3))
print(find_first_k_missing_positive([2, 3, 4], k=3))
print(find_first_k_missing_positive([-2, -3, 4], k=2))
