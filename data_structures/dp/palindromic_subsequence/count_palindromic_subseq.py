"""
Count palindromic subseq. of a give string.
"""


def count_palin_subseq_dp_bottom_up_tabular(string):
    n = len(string)
    if n == 0:
        return -1

    dp = [[0 for i in range(n)] for j in range(n)]

    for j in range(n):
        dp[j][j] = 1

    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                dp[start][end] = 1 + dp[start + 1][end] + dp[start][end - 1]
            else:
                dp[start][end] = 1 + max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1]


print("======== count palindromic subseq dp bottom up tabular ==========")
print(count_palin_subseq_dp_bottom_up_tabular("abcd"))
print(count_palin_subseq_dp_bottom_up_tabular("aab"))
print(count_palin_subseq_dp_bottom_up_tabular("aaaa"))
print(count_palin_subseq_dp_bottom_up_tabular("abcb"))
print(count_palin_subseq_dp_bottom_up_tabular("aba"))
