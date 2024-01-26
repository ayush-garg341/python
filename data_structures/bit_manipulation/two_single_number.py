"""
Given an arr of nums, where each num occur twice,
except two.
Find those two nums which occurs only once.

Steps:
    1. Find XOR of all numbers
    2. Find right most set bit mask of above XOR
        - xor & -xor
    3. Now we know that out of two single occurring nums,
        one has 0 and other has 1 in it.
"""


def two_single_numbers(arr):
    bitwise_xor = 0
    for num in arr:
        bitwise_xor ^= num  # will left with XOR of two single nums
    rbm = bitwise_xor & -bitwise_xor
    result = 0
    for num in arr:
        if rbm & num == rbm:  # getting num which has rmbs -> 1
            result ^= num

    return [result, result ^ bitwise_xor]


print(two_single_numbers([1, 2, 2, 3, 3, 4]))
print(two_single_numbers([4, 1, 2, 1, 2, 0]))
