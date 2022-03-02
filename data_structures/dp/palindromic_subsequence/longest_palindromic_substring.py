"""
Given a string, find the length of its Longest Palindromic Substring (LPS).
In a palindromic string, elements read the same backward and forward.

example1:
    Input: "abdbca"
    Output: 3
    Explanation: LPS is "bdb".

example2:
    Input: = "cddpd"
    Output: 3
    Explanation: LPS is "dpd".

example3:
    Input: = "pqr"
    Output: 1
    Explanation: LPS could be "p", "q" or "r".
"""


def lps_brute_force(string):
    n = len(string)
    if n == 0:
        return -1
    start = 0
    end = n - 1
    return lps_brute_force_recursive(string, start, end)


def lps_brute_force_recursive(string: str, start: int, end: int) -> int:
    if start == end:
        return 1

    if start > end:
        return 0

    count1, count2 = 0, 0
    if string[start] == string[end]:
        remaining_len = end - start - 1
        if remaining_len == lps_brute_force_recursive(string, start + 1, end - 1):
            return 2 + remaining_len
    count1 = lps_brute_force_recursive(string, start + 1, end)
    count2 = lps_brute_force_recursive(string, start, end - 1)

    return max(count1, count2)


print("======== max lps burte force recursive =========")
print(lps_brute_force("abdba"))
print(lps_brute_force("abdbca"))
print(lps_brute_force("cddpd"))
print(lps_brute_force("pqr"))


def lps_dp_top_bottom(string):
    n = len(string)
    dp = [[0 for i in range(n)] for j in range(n)]
    return lps_dp_top_bottom_recursive(string, dp, 0, len(string) - 1)


def lps_dp_top_bottom_recursive(string: str, dp: list, start: int, end: int):
    if start == end:
        return 1
    if start > end:
        return 0

    if dp[start][end] == 0:
        if string[start] == string[end]:
            remaining_len = end - start - 1
            if remaining_len == lps_dp_top_bottom_recursive(
                string, dp, start + 1, end - 1
            ):
                dp[start][end] = 2 + remaining_len
                return dp[start][end]

        count1 = lps_dp_top_bottom_recursive(string, dp, start + 1, end)
        count2 = lps_dp_top_bottom_recursive(string, dp, start, end - 1)
        dp[start][end] = max(count1, count2)

    return dp[start][end]


print("======== max lps dp top bottom =========")
print(lps_dp_top_bottom("abdba"))
print(lps_dp_top_bottom("abdbca"))
print(lps_dp_top_bottom("cddpd"))
print(lps_dp_top_bottom("pqr"))


def lps_dp_bottom_up_tabular(string):
    n = len(string)
    if n == 0:
        return -1

    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(string)):
        dp[i][i] = 1

    for start in range(n - 2, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                remaining_len = end - start - 1
                if remaining_len == dp[start + 1][end - 1]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1]


print("======== max lps dp bottom up tabular =========")
print(lps_dp_bottom_up_tabular("abdba"))
print(lps_dp_bottom_up_tabular("abdbca"))
print(lps_dp_bottom_up_tabular("cddpd"))
print(lps_dp_bottom_up_tabular("pqr"))
