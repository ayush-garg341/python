"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of
the square of all of its digits, leads us to number ‘1’.

example1:
    Input: 23
    Output: true (23 is a happy number)
    Explanations: Here are the steps to find out that 23 is a happy number

example2:
    Input: 12
    Output: false (12 is not a happy number)
    Explanations: Here are the steps to find out that 12 is not a happy number
"""


def happy_number(num):
    slow = sum_of_squares_of_digits(num)
    fast = sum_of_squares_of_digits(sum_of_squares_of_digits(num))

    if slow == 1 or fast == 1:
        return True

    while slow != fast:
        slow = sum_of_squares_of_digits(slow)
        fast = sum_of_squares_of_digits(sum_of_squares_of_digits(fast))
        if slow == fast:
            return False
        elif slow == 1 or fast == 1:
            return True

    return False


def sum_of_squares_of_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        num = int(num / 10)
        sum += rem * rem

    return sum


print(happy_number(23))
print(happy_number(12))
