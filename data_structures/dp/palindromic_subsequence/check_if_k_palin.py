"""
Any string will be called K-palindromic if it can be transformed
into a palindrome by removing at most ‘K’ characters from it.

It follows the same pattern as min deletions to make palin.
If the “minimum deletion count” is not more than ‘K’, the string will be K-Palindromic.
"""


def check_k_palin(string: str, k: int) -> bool:
    n = len(string)
    if n == 0:
        return False

    dp = [[0 for i in range(n)] for j in range(n)]

    for start in range(n - 2, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1] <= k


print("======== check k palin dp bottom up tabular ==========")
print(check_k_palin("abdbca", 2))
print(check_k_palin("cddpd", 3))
print(check_k_palin("pqr", 1))
print(check_k_palin("abcdcba", 0))
