"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

example1:
    Input: s1 = "abdca"
           s2 = "cbda"
    Output: 3
    Explanation: The longest common subsequence is "bda".

example2:
    Input: s1 = "passport"
           s2 = "ppsspt"
    Output: 5
    Explanation: The longest common subsequence is "psspt".

"""


def longest_common_subseq_brute_force(s1: str, s2: str):
    count = longest_common_subseq_brute_force_recursive(s1, s2, 0, 0)
    return count


def longest_common_subseq_brute_force_recursive(
    s1: str, s2: str, i: int, j: int
) -> int:
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        return 1 + longest_common_subseq_brute_force_recursive(s1, s2, i + 1, j + 1)

    count1 = longest_common_subseq_brute_force_recursive(s1, s2, i + 1, j)
    count2 = longest_common_subseq_brute_force_recursive(s1, s2, i, j + 1)

    return max(count1, count2)


print("====== longest common subseq brute force ========")
print(longest_common_subseq_brute_force("abdca", "cbda"))
print(longest_common_subseq_brute_force("passport", "ppsspt"))


def longest_common_subseq_dp_top_bottom(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 == 0 or n2 == 0:
        return -1
    dp = [[-1 for i in range(n2)] for j in range(n1)]
    count = longest_common_subseq_dp_top_bottom_recursive(s1, s2, dp, 0, 0)
    return count


def longest_common_subseq_dp_top_bottom_recursive(
    s1: str, s2: str, dp: list, i: int, j: int
):
    if i == len(s1) or j == len(s2):
        return 0

    if dp[i][j] == -1:
        if s1[i] == s2[j]:
            dp[i][j] = 1 + longest_common_subseq_dp_top_bottom_recursive(
                s1, s2, dp, i + 1, j + 1
            )
        else:
            count1 = longest_common_subseq_dp_top_bottom_recursive(s1, s2, dp, i, j + 1)
            count2 = longest_common_subseq_dp_top_bottom_recursive(s1, s2, dp, i + 1, j)
            dp[i][j] = max(count1, count2)
    return dp[i][j]


print("====== longest common subseq dp top bottom  ========")
print(longest_common_subseq_dp_top_bottom("abdca", "cbda"))
print(longest_common_subseq_dp_top_bottom("passport", "ppsspt"))
print(longest_common_subseq_dp_top_bottom("ppp", "ppp"))


def longest_common_subseq_dp_bottom_up_tabular(s1: str, s2: str):
    n1, n2 = len(s1), len(s2)
    if n1 == 0 or n2 == 0:
        return -1

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for start in range(1, n1 + 1):
        for end in range(1, n2 + 1):
            if s1[start - 1] == s2[end - 1]:
                dp[start][end] = 1 + dp[start - 1][end - 1]
            else:
                dp[start][end] = max(dp[start - 1][end], dp[start][end - 1])

    return dp[n1][n2]


print("====== longest common subseq dp bottom up tabular ========")
print(longest_common_subseq_dp_bottom_up_tabular("abdca", "cbda"))
print(longest_common_subseq_dp_bottom_up_tabular("passport", "ppsspt"))
