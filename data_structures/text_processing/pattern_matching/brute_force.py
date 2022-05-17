"""
Brute force approach to find the pattern p in string s.
Return the first matching index of the pattern p in s.
"""


from typing import List


def brute_force(string: str, pattern: str) -> List[int]:
    result = []

    m = len(string)
    n = len(pattern)
    if m < n:
        return result
    for i in range(m - n + 1):
        k = 0

        while k < n and string[i + k] == pattern[k]:
            k += 1
        if k == n:
            result.append(i)

    return result


print(brute_force("ayushgarggarg", "gar"))
