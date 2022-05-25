"""
Better than naive algorithm. This algorithm uses two heuristics to skip un-necessary comparisons between text and pattern.

    - Begin comparisons from the last char in the pattern instead of first char and move backwards.
    - If the character in text mismatches in the pattern:-
        - If the mismatched char is not found in pattern then move text pointer i past the whole pattern.
        - If the mismatched char is present in pattern then move the text pointer i past that index in pattern.
"""


def find_booyer_moore(string: str, pattern: str) -> int:
    m = len(string)
    n = len(pattern)
    i = n - 1
    j = n - 1

    if m < n:
        return -1

    last = {}
    for i in range(n):
        last[pattern[i]] = i

    while i < m:
        if string[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i = i - 1
                j = j - 1

        else:
            idx = last.get(string[i], -1)
            i += n - min(j, idx + 1)
            j = n - 1

    return -1


print(find_booyer_moore("ayushgarggarg", "gar"))
print(find_booyer_moore("ayushgarggarg", "abcd"))
print(find_booyer_moore("ayushgarggabcdga", "abcd"))
