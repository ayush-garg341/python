"""
XOR properites
    1. x ^ x = 0
    2. x ^ 0 = x
    3. a ^ (b ^ c) = (a ^ b) ^ c
    4. a ^ b = b ^ a
"""


def find_missing_number(nums):
    """
    Given an array of integers from 1 to n find missing number.
    ex1: nums = [1, 2, 3, 5]
        missing number = 4
    ex2: nums = [1, 3, 4, 5]
        missing number = 2
    """

    n = len(nums)
    xor = 0
    for num in nums:
        xor = xor ^ num

    for i in range(1, n + 2):
        xor = xor ^ i

    return xor


print(find_missing_number([1, 2, 3, 5]))
print(find_missing_number([1, 3, 4, 5]))
print(find_missing_number([1, 2, 3, 4]))


def find_single_number(nums):
    xor = 0
    for num in nums:
        xor = xor ^ num
    return xor


arr = [1, 4, 2, 1, 3, 2, 3]
print(find_single_number(arr))
