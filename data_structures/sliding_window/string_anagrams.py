"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
Every anagram is a permutation of a string.

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

example1:
    Input: String="ppqp", Pattern="pq"
    Output: [1, 2]
    Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

example2:
    Input: String="abbcabc", Pattern="abc"
    Output: [2, 3, 4]
    Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""


def find_string_anagrams_indexes(string: str, pattern: str) -> list:
    results = []
    pattern_freq = get_pattern_char_freq(pattern)
    matched = 0
    window_start = 0
    window_end = 0
    while window_end < len(string):
        right_char = string[window_end]
        if right_char in pattern_freq:
            pattern_freq[right_char] -= 1
            if pattern_freq[right_char] == 0:
                matched += 1

        if matched == len(pattern_freq):
            results.append(window_start)
            window_start += 1
            window_end = window_start
            pattern_freq = get_pattern_char_freq(pattern)
            matched = 0
            continue

        if window_end - window_start + 1 >= len(pattern):
            left_char = string[window_start]
            if left_char in pattern_freq:
                if pattern_freq[left_char] == 0:
                    matched -= 1
                pattern_freq[left_char] += 1
            window_start += 1

        window_end += 1

    return results


def get_pattern_char_freq(pattern: str) -> dict:
    char_freq = {}
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0

        char_freq[char] += 1

    return char_freq


print(find_string_anagrams_indexes("ppqp", "pq"))
print(find_string_anagrams_indexes("abbcabc", "abc"))


def string_anagram_index(string: str, pattern: str):
    window_start = 0
    results = []
    matched = 0

    char_freq = {}
    for char in pattern:
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
            results.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

            window_start += 1

    return results


print(string_anagram_index("ppqp", "pq"))
print(string_anagram_index("abbcabc", "abc"))
