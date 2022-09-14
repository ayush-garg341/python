# This  is test file.

"""
input -> "python is my fav language"
output -> "language fav my is python"
"""


def reverse_words_in_string(string):
    reverse_string = ""

    n = len(string)

    print("len of original string is : ", n)

    for i in range(n-1, -1, -1):
        reverse_string += string[i]

    print("len of reversed string is : ", len(reverse_string))

    reverse_word_by_word = ""

    start = -1
    end = -1
    white_space = True

    for j in range(n):
        if reverse_string[j] != " ":
            end += 1
            white_space = False
        else:
            if not white_space:
                for char in range(end, start, -1):
                    reverse_word_by_word += reverse_string[char]
            white_space = True
            reverse_word_by_word += " "
            start = j
            end = j

    if not white_space:
        for char in range(end, start, -1):
            reverse_word_by_word += reverse_string[char]

    print("reverse word by word : ", len(reverse_word_by_word))

    return reverse_word_by_word

# inp = "python is my fav language"
# print(reverse_words_in_string(inp))

# inp2 = "I love c  "
# print(reverse_words_in_string(inp2))

# inp3 = "  I hate JS  "
# print(reverse_words_in_string(inp3))


def find_permutation(string, pattern):
    pattern_dict = {}
    total_match = 0
    pattern_len = len(pattern)
    for char in pattern:
        if char not in pattern_dict:
            pattern_dict[char] = 0
        pattern_dict[char] += 1
    window_start = 0
    for window_end in range(len(string)):
        char = string[window_end]
        if char in pattern_dict:
            pattern_dict[char] -= 1
            if pattern_dict[char] == 0:
                total_match += 1

        if total_match == len(pattern_dict):
            return True
        if window_end - window_start + 1 == pattern_len:
            start_char = string[window_start]
            if start_char in pattern_dict:
                if pattern_dict[start_char] == 0:
                    total_match -= 1
                pattern_dict[start_char] += 1
            window_start += 1

    return False

# print(find_permutation("eidbaooo", "ab"))
# print(find_permutation("ooolleoooleh", "hello"))
# print(find_permutation("dcda", "adc"))



def longest_subsseq(str1, str2):
    longest = longest_subsseq_rec(str1, str2, 0, 0)
    return longest

def longest_subsseq_rec(str1, str2, i, j):
    if len(str1) == i or len(str2) == j:
        return 0

    if str1[i] == str2[j]:
        return 1 + longest_subsseq_rec(str1, str2, i+1, j+1)

    count1 = longest_subsseq_rec(str1, str2, i+1, j)
    count2 = longest_subsseq_rec(str1, str2, i, j+1)

    return max(count1, count2)

# print(longest_subsseq("ZXVVYZW", "XKYKZPW"))
# print(longest_subsseq("ABCDEFG", "APPLES"))

from collections import deque

def longest_subsseq_tabulation(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    dp = [[0 for j in range(n1+1)] for i in range(n2+1)]

    for i in range(1, n2+1):
        for j in range(1, n1+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    output = deque()

    i = n2
    j = n1
    while i >= 1 and j >= 1:
        if dp[i][j] != dp[i-1][j] and dp[i][j] != dp[i][j-1]:
            output.appendleft(str2[i-1])
            i = i - 1
            j = j - 1
        else:
            if dp[i][j] == dp[i-1][j]:
                i = i-1
            elif dp[i][j] == dp[i][j-1]:
                j = j - 1
    return list(output)


# print(longest_subsseq_tabulation("ZXVVYZW", "XKYKZPW"))
# print(longest_subsseq_tabulation("ABCDEFG", "APPLES"))



def longest_subsseq_tabulation_another_method(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    dp = [[[None, 0, None, None] for j in range(n1+1)] for i in range(n2+1)]

    for i in range(1, n2+1):
        for j in range(1, n1+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = [str1[j-1], 1 + dp[i-1][j-1][1], i-1, j-1]
            else:
                if dp[i-1][j][1] > dp[i][j-1][1]:
                    dp[i][j] = [None, dp[i-1][j][1], i-1, j]
                else:
                    dp[i][j] = [None, dp[i][j-1][1], i, j-1]

    i = n2
    j = n1
    result = []
    while i!=0 and j!=0:
        current_record = dp[i][j]
        if current_record[0] is not None:
            result.append(current_record[0])
        i = current_record[2]
        j = current_record[3]
    return list(reversed(result))

# print(longest_subsseq_tabulation_another_method("ZXVVYZW", "XKYKZPW"))
# print(longest_subsseq_tabulation_another_method("ABCDEFG", "APPLES"))

import math
def minWindow(str1: str, pattern: str) -> str:
    pat_map = {}
    for char in pattern:
        if char not in pat_map:
            pat_map[char] = 0
        pat_map[char] += 1
    window_start = 0
    match_len = 0
    min_len = math.inf
    start_window = 0
    for window_end in range(len(str1)):
        char = str1[window_end]
        if char in pat_map:
            pat_map[char] -= 1
            if pat_map[char] == 0:
                match_len += 1

        while match_len == len(pat_map):
            start_char = str1[window_start]
            if start_char in pat_map:
                if pat_map[start_char] == 0:
                    match_len -= 1
                pat_map[start_char] += 1
            if window_end - window_start + 1 < min_len:
                min_len = window_end - window_start + 1
                start_window = window_start
            # min_len = min(min_len, window_end - window_start + 1)
            window_start += 1
    substr = ""
    if min_len != math.inf:
        end = start_window + min_len
        return str1[start_window: end]
    return substr

print(minWindow("cabwefgewcwaefgcf","cae"))
