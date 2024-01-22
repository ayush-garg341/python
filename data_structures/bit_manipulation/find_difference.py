"""
Given two strings, str1 and str2, find the index of the extra
character that is present in only one of the strings.

If multiple instances of the extra character exist, return the
index of the first occurrence of the character in the longer string.
"""


def extra_character_index(str1, str2):
    idx = -1
    result = 0
    for char in str1:
        result ^= ord(char)

    for char in str2:
        result ^= ord(char)
    missing_char = chr(result)

    if len(str1) > len(str2):
        for char in str1:
            idx += 1
            if char == missing_char:
                return idx
    else:
        for char in str2:
            idx += 1
            if char == missing_char:
                return idx
    return idx


print(extra_character_index("mpon", "mno"))
print(extra_character_index("wxyz", "wxytz"))
