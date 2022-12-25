"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

example1:
    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

example2:
    Input: word1 = "leetcode", word2 = "etco"
    Output: 4
"""


def min_distance(word1: str, word2: str) -> int:
    n2 = len(word2)
    n1 = len(word1)
    dp = [[-1 for i in range(n2)] for j in range(n1)]
    return len(word1) + len(word2) - 2 * longest_common_subseq(word1, word2, dp, 0, 0)


def longest_common_subseq(
    word1: str, word2: str, dp, index_1: int, index_2: int
) -> int:
    if index_1 == len(word1):
        return 0

    if index_2 == len(word2):
        return 0

    if dp[index_1][index_2] != -1:
        return dp[index_1][index_2]

    count1, count2 = 0, 0
    if word1[index_1] == word2[index_2]:
        return 1 + longest_common_subseq(word1, word2, dp, index_1 + 1, index_2 + 1)

    count1 = longest_common_subseq(word1, word2, dp, index_1 + 1, index_2)
    count2 = longest_common_subseq(word1, word2, dp, index_1, index_2 + 1)
    dp[index_1][index_2] = max(count1, count2)

    return dp[index_1][index_2]


print(min_distance("sea", "eat"))
print(min_distance("sea", "ate"))
print(min_distance("leetcode", "etco"))
