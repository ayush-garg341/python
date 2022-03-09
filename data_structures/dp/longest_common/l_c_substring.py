"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

example1:
    Input: s1 = "abdca"
           s2 = "cbda"
    Output: 2
    Explanation: The longest common substring is "bd".

example2:
    Input: s1 = "passport"
           s2 = "ppsspt"
    Output: 3
    Explanation: The longest common substring is "ssp".
"""


def longest_common_substr_brute_force(s1: str, s2: str):
    count = longest_common_substr_brute_force_recursive(s1, s2, 0, 0, 0)
    return count


def longest_common_substr_brute_force_recursive(
    s1: str, s2: str, i: int, j: int, count: int
) -> int:
    if i == len(s1) or j == len(s2):
        return count

    if s1[i] == s2[j]:
        count = longest_common_substr_brute_force_recursive(
            s1, s2, i + 1, j + 1, count + 1
        )

    count1 = longest_common_substr_brute_force_recursive(s1, s2, i + 1, j, 0)
    count2 = longest_common_substr_brute_force_recursive(s1, s2, i, j + 1, 0)

    return max(count, max(count1, count2))


print("============= longest common substr brute force ==========")
print(longest_common_substr_brute_force("abdca", "cbda"))
print(longest_common_substr_brute_force("passport", "ppsspt"))


# def longest_common_substr_dp_top_bottom(s1: str, s2: str):
# n1 = len(s1)
# n2 = len(s2)
# if n1 == 0 or n2 == 0:
# return -1
# min_len = min(n1, n2)
# max_len = max(n1, n2)
# dp = [
# [[-1 for _ in range(min_len)] for _ in range(max_len)] for _ in range(max_len)
# ]
# count = longest_common_substr_dp_top_bottom_recursive(s1, s2, dp, 0, 0, 0)
# return count


# def longest_common_substr_dp_top_bottom_recursive(
# s1: str, s2: str, dp: list, i: int, j: int, count: int
# ) -> int:
# if i == len(s1) or j == len(s2):
# return count

# if dp[i][j][count] == -1:
# if s1[i] == s2[j]:
# count = longest_common_substr_dp_top_bottom_recursive(
# s1, s2, dp, i + 1, j + 1, count + 1
# )

# count1 = longest_common_substr_dp_top_bottom_recursive(s1, s2, dp, i + 1, j, 0)
# count2 = longest_common_substr_dp_top_bottom_recursive(s1, s2, dp, i, j + 1, 0)

# dp[i][j][count] = max(count, max(count1, count2))

# return dp[i][j][count]


# print("============= longest common substr dp top bottom ==========")
# print(longest_common_substr_dp_top_bottom("abdca", "cbda"))
# print(longest_common_substr_dp_top_bottom("passport", "ppsspt"))


def longest_common_substr_dp_bottom_up_tabular(s1: str, s2: str):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == 0 or n2 == 0:
        return -1

    dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

    max_count = 0
    for start in range(1, n2 + 1):
        for end in range(1, n1 + 1):
            if s2[start - 1] == s1[end - 1]:
                dp[start][end] = 1 + dp[start - 1][end - 1]
                max_count = max(dp[start][end], max_count)

    return max_count


print("============= longest common substr dp bottom up tabular ==========")
print(longest_common_substr_dp_bottom_up_tabular("abdca", "cbda"))
print(longest_common_substr_dp_bottom_up_tabular("passport", "ppsspt"))
