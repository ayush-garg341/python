"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

example1:
    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.

example2:
    Input: String="odicf", Pattern="dc"
    Output: false
    Explanation: No permutation of the pattern is present in the given string as a substring.
"""


def permutation_in_string(string: str, pattern: str) -> bool:
    window_start = 0
    pattern_len = len(pattern)
    char_freq = {}
    matched = 0
    for i in range(pattern_len):
        char = pattern[i]
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        if matched == len(char_freq):
            return True

        if window_end >= pattern_len - 1:
            left_char = string[window_start]
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

            window_start += 1

    return False


print(permutation_in_string("oidbcaf", "abc"))
print(permutation_in_string("odicf", "dc"))
print(permutation_in_string("bcdxabcdy", "bcdyabcdx"))
print(permutation_in_string("aaacb", "abc"))
