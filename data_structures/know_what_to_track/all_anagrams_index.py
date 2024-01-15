"""
Given two strings, a and b, return an array of all the start indexes
of anagrams of b in a. We may return the answer in any order.
"""

from collections import defaultdict


def find_anagrams(a, b):
    result = []
    if len(b) > len(a):
        return result
    hash_a = defaultdict(int)
    hash_b = defaultdict(int)

    for char in b:
        hash_b[char] += 1
    window_start = 0
    for window_end in range(len(a)):
        if window_end >= len(b):
            if hash_a == hash_b:
                result.append(window_start)
            if hash_a[a[window_start]] == 1:
                del hash_a[a[window_start]]
            else:
                hash_a[a[window_start]] -= 1
            window_start += 1

        hash_a[a[window_end]] += 1

    if hash_a == hash_b:
        result.append(window_start)

    return result


print(find_anagrams("abab", "ab"))
print(find_anagrams("cbaebabacd", "abc"))
