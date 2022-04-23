"""
We are given an array containing n distinct numbers taken from the range 0 to n.
Since the array has only n numbers out of the total n+1 numbers, find the missing number.

example1:
    Input: [4, 0, 3, 1]
    Output: 2

example2:
    Input: [8, 3, 5, 2, 4, 6, 0, 1]
    Output: 7
"""


def find_missing_number_using_sum(nums):
    # TODO: Write your code here
    n = len(nums)
    s = int((n * (n + 1)) / 2)
    arr_sum = sum(nums)
    return s - arr_sum


print(find_missing_number_using_sum([4, 0, 3, 1]))
print(find_missing_number_using_sum([8, 3, 5, 2, 4, 6, 0, 1]))


def find_missing_number_using_set(nums):
    set_num = set()
    for num in nums:
        set_num.add(num)

    for i in range(len(nums) + 1):
        if i not in set_num:
            return i


print(" ================ ")
print(find_missing_number_using_set([4, 0, 3, 1]))
print(find_missing_number_using_set([8, 3, 5, 2, 4, 6, 0, 1]))


def find_missing_number(nums):
    i = 0
    n = len(nums)
    while i < n:
        num = nums[i]
        if i != nums[i] and num <= n - 1:
            index = nums[i]
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)


print(" ================ ")
print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number([7, 3, 5, 2, 4, 6, 0, 1]))
