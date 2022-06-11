"""
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
Find the two numbers that appear only once.

example1:
    Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
    Output: [4, 6]

example2:
    Input: [2, 1, 3, 2]
    Output: [1, 3]
"""


def find_single_numbers(nums):
    n1xn2 = 0
    for num in nums:
        n1xn2 = n1xn2 ^ num

    rightmostsetbit = 1
    while n1xn2 & rightmostsetbit == 0:
        rightmostsetbit = rightmostsetbit << 1
    num1, num2 = 0, 0
    for num in nums:
        if rightmostsetbit & num != 0:
            num1 = num1 ^ num
        else:
            num2 = num2 ^ num
    return [num1, num2]


def main():
    print("Single numbers are:" + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print("Single numbers are:" + str(find_single_numbers([2, 1, 3, 2])))


main()
