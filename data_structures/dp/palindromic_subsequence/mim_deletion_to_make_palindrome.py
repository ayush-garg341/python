"""
Given a string, find the minimum number of characters that we can remove to make it a palindrome.

example1:
    Input: "abdbca"
    Output: 1
    Explanation: By removing "c", we get a palindrome "abdba".

example2:
    Input: = "cddpd"
    Output: 2
    Explanation: Deleting "cp", we get a palindrome "ddd".

example3:
    Input: = "pqr"
    Output: 2
    Explanation: We have to remove any two characters to get a palindrome, e.g. if we
    remove "pq", we get palindrome "r".
"""


def min_deletion_to_make_palin_dp_bottoms_up_tabular(string):
    n = len(string)
    if n == 0:
        return -1

    dp = [[0 for i in range(n)] for j in range(n)]

    for start in range(n - 2, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1]


print("============= min deletion to make palin dp bottom up tabular =============")

print(min_deletion_to_make_palin_dp_bottoms_up_tabular("abdbca"))
print(min_deletion_to_make_palin_dp_bottoms_up_tabular("cddpd"))
print(min_deletion_to_make_palin_dp_bottoms_up_tabular("pqr"))
print(min_deletion_to_make_palin_dp_bottoms_up_tabular("abcdcba"))
