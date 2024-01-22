"""
For any n positive number in base 10, return the complement
of its binary representation as an integer in base 10.
"""

import math


def find_bitwise_complement(n):
    if n == 0:
        return 1
    bits_count = math.floor(math.log2(n)) + 1
    bits_set_num = int(math.pow(2, bits_count) - 1)
    return bits_set_num ^ n


print(find_bitwise_complement(42))
print(find_bitwise_complement(8))
