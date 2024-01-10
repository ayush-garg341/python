"""
Length of longest palindromic substring by composing chars of string.
"""


def longest_palindrome(s):
    if len(s) == 1:
        return 1

    longest_len = 0
    freq_map = dict()
    for char in s:
        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1
    for k, v in freq_map.items():
        longest_len += (v // 2) * 2
    if longest_len < len(s):
        longest_len += 1
    return longest_len
