"""
Given a string and a pattern, find the smallest substring in the given string which has all
the character occurrences of the given pattern.

example1:
    Input: String="aabdec", Pattern="abc"
    Output: "abdec"
    Explanation: The smallest substring having all characters of the pattern is "abdec"

example2:
    Input: String="aabdec", Pattern="abac"
    Output: "aabdec"
    Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"
"""


def find_substring(string: str, pattern: str):
    window_start = 0
    char_freq = {}
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    substr = ""
    substr_len = len(string) + 1
    matched_count = 0
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched_count += 1

        while matched_count == len(char_freq):
            len_substr = window_end - window_start + 1
            if len_substr < substr_len:
                substr = string[window_start : window_end + 1]

            left_char = string[window_start]
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched_count -= 1
                char_freq[left_char] += 1
            window_start += 1
    return substr


print(find_substring("aaaaabcdecccc", "abc"))
# print(find_substring("abdbca", "abc"))
# print(find_substring("aabdec", "abac"))
# print(find_substring("adcad", "abc"))
