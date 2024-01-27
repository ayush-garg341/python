"""
Reverse bits of a number.
"""


def reverse_bits(num):
    NUM_BITS = 32
    result = 0
    for i in range(NUM_BITS):
        if num & (1 << i):
            result |= 1 << (NUM_BITS - 1 - i)

    return result


print(reverse_bits(43261596))
print(reverse_bits(5))
print(reverse_bits(41596))
