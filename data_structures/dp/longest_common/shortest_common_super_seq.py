"""
Given two sequences ‘s1’ and ‘s2’, write a method to find the
length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

example1:
    Input: s1: "abcf" s2:"bdcf"
    Output: 5
    Explanation: The shortest common super-sequence (SCS) is "abdcf".

example2:
    Input: s1: "dynamic" s2:"programming"
    Output: 15
    Explanation: The SCS is "dynprogrammicng".

Approach -> We can calculate LC subseq. ex. c
shortest common superseq = n1-c + n2-c + c

Approach2 -> we can process both of the sequences one character at a time, so at any step, we must choose between:

    1. If the sequences have a matching character, we can skip one character from both the sequences and make a recursive call for the remaining lengths to get SCS.
    2. If the strings don’t match, we start two new recursive calls by skipping one character separately from each string. The minimum of these two recursive calls will have our answer.
"""


def shortest_common_super_seq_brute_force(s1, s2):
    return shortest_common_super_seq_brute_force_recursive(s1, s2, 0, 0)


def shortest_common_super_seq_brute_force_recursive(s1: str, s2: str, i: int, j: int):
    n1, n2 = len(s1), len(s2)
    if i == n1:
        return n2 - j
    if j == n2:
        return n1 - i

    if s1[i] == s2[j]:
        return 1 + shortest_common_super_seq_brute_force_recursive(s1, s2, i + 1, j + 1)

    len1 = 1 + shortest_common_super_seq_brute_force_recursive(s1, s2, i, j + 1)
    len2 = 1 + shortest_common_super_seq_brute_force_recursive(s1, s2, i + 1, j)

    return min(len1, len2)


print("========= shortest common superseq length brute force =========")
print(shortest_common_super_seq_brute_force("abcf", "bdcf"))
print(shortest_common_super_seq_brute_force("dynamic", "programming"))


def shortest_common_super_seq_dp_bottom_up_tabular(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 == 0 or n2 == 0:
        return n1 if n2 == 0 else n2

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    longest_common_subseq = dp[n1][n2]
    return n1 + n2 - longest_common_subseq


print("========= shortest common superseq length dp bottom up tabular =========")
print(shortest_common_super_seq_dp_bottom_up_tabular("abcf", "bdcf"))
print(shortest_common_super_seq_dp_bottom_up_tabular("dynamic", "programming"))
