"""
Return longest palindromic substring not just length
"""


def longestPalindromicSubstring(string):
    """
    Calculating the length of longest palindromic substring first and then from that getting the substring.
    """
    # Write your code here.
    n = len(string)
    if n == 0 or n == 1:
        return string

    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for start in range(n - 2, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                rem_len = end - start - 1
                if rem_len == dp[start + 1][end - 1]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    length = dp[0][n - 1]
    end_idx = -1
    for i in range(n - 1, -1, -1):
        if dp[0][i] == length:
            continue
        else:
            end_idx = i + 1
            break
    start = end_idx - length + 1
    return string[start : end_idx + 1]


print(longestPalindromicSubstring("abaxyzzyxf"))


def longest_palin_susbtr_without_cal_len(string):
    n = len(string)
    if n == 0 or n == 1:
        return string

    char = string[0]
    dp = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if string[i] != string[j]:
                continue
            else:
                if dp[i + 1][j - 1] or j - i == 1:
                    dp[i][j] = True
                    if len(char) < j - i + 1:
                        char = string[i : j + 1]

    return char


print(longest_palin_susbtr_without_cal_len("abaxyzzyxf"))
