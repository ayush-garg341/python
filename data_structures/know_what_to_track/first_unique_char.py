"""
For a given string of characters, s, your task is to find the first
non-repeating character and return its index.

Return −1 if there’s no unique character in the given string.
"""

from collections import defaultdict


def first_unique_sorted_char(s):
    chars = [0] * 26
    for char in s:
        idx = ord(char) - ord("a")
        chars[idx] += 1

    for idx in range(len(chars)):
        val = chars[idx]
        if val == 1:
            return chr(idx + ord("a"))

    return -1


print(first_unique_sorted_char("awsjawuh"))
print(first_unique_sorted_char("weiieow"))


def first_unique_char(s):
    chars = [0] * 26
    for char in s:
        idx = ord(char) - ord("a")
        chars[idx] += 1

    for i in range(len(s)):
        char = s[i]
        idx = ord(char) - ord("a")
        if chars[idx] == 1:
            return i
    return -1


print(first_unique_char("awsjawuh"))
print(first_unique_char("weiieow"))
print(first_unique_char("goodmorning"))
