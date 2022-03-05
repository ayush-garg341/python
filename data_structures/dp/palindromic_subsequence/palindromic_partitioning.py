"""
Given a string, we want to cut it into pieces such that each piece is a palindrome.
Write a function to return the minimum number of cuts needed.

example1:
    Input: "abdbca"
    Output: 3
    Explanation: Palindrome pieces are "a", "bdb", "c", "a".

example2:
    Input: = "cddpd"
    Output: 2
    Explanation: Palindrome pieces are "c", "d", "dpd".

example3:
    Input: = "pqr"
    Output: 2
    Explanation: Palindrome pieces are "p", "q", "r".
"""


# def count_palindromic_cuts_dp_top_bottom(string):
# n = len(string)
# if n == 0:
# return -1
# dp = [[0 for i in range(n)] for j in range(n)]

# start = 0
# end = len(string) - 1
# count = count_palindromic_cuts_dp_top_bottom_recursive(string, dp, start, end)
# return count


# def count_palindromic_cuts_dp_top_bottom_recursive(
# string: str, dp: list, start: int, end: int
# ):
# if end - start - 1 == 0 and string[start] != string[end]:
# return 1

# if start >= end:
# return 0

# if dp[start][end] == 0:
# if string[start] == string[end]:
# remaining_len = end - start - 1
# if remaining_len == count_palindromic_cuts_dp_top_bottom_recursive(
# string, dp, start + 1, end - 1
# ):
# dp[start][end] = 0

# count1 = count_palindromic_cuts_dp_top_bottom_recursive(
# string, dp, start + 1, end
# )
# count2 = count_palindromic_cuts_dp_top_bottom_recursive(
# string, dp, start, end - 1
# )
# dp[start][end] = min(count1, count2)

# return dp[start][end]


# print("========= count palindrome cuts dp top bottom recursive =======")
# # print(count_palindromic_cuts_dp_top_bottom("abdbca"))
# # print(count_palindromic_cuts_dp_top_bottom("cddpd"))
# print(count_palindromic_cuts_dp_top_bottom("pqr"))
# print(count_palindromic_cuts_dp_top_bottom("pp"))


def count_palindromic_cuts_dp_bottom_up_tabular(string):
    n = len(string)
    if n == 0:
        return -1

    dp = [[0 for i in range(n)] for j in range(n)]

    for start in range(n - 2, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                if dp[start + 1][end - 1] == 0:
                    dp[start][end] = 0
                else:
                    dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])
            else:
                dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1]


print("========= count palindrome cuts dp bottom up tabular =======")
print(count_palindromic_cuts_dp_bottom_up_tabular("abdbca"))
print(count_palindromic_cuts_dp_bottom_up_tabular("cddpd"))
print(count_palindromic_cuts_dp_bottom_up_tabular("pqr"))
print(count_palindromic_cuts_dp_bottom_up_tabular("pp"))
