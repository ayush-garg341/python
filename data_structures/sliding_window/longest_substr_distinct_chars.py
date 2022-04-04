"""
Given a string, find the length of the longest substring, which has all distinct characters.

example1:
    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring with distinct characters is "abc".

example2:
    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring with distinct characters is "ab".

example3:
    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""


def non_repeat_str(string: str):
    window_start = 0
    max_len = 0

    distinct = {}
    for window_end in range(len(string)):
        char = string[window_end]
        if char not in distinct:
            distinct[char] = 0
        distinct[char] += 1

        while len(distinct) != window_end - window_start + 1:
            left_char = string[window_start]
            distinct[left_char] -= 1
            if distinct[left_char] == 0:
                del distinct[left_char]

            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


print(non_repeat_str("aabccbb"))
print(non_repeat_str("abbbb"))
print(non_repeat_str("abccde"))
