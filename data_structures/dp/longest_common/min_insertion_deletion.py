"""
Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
Write a function to calculate the count of the minimum number of deletion and insertion operations.

example1:
    Input: s1 = "abc"
           s2 = "fbc"
    Output: 1 deletion and 1 insertion.
    Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

example2:
    Input: s1 = "abdca"
           s2 = "cbda"
    Output: 2 deletions and 1 insertion.
    Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

example3:
    Input: s1 = "passport"
           s2 = "ppsspt"
    Output: 3 deletions and 1 insertion
    Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.

This problems follow the Longest common subseq pattern. Let say LCS is 5
Deletion = len(s1) - 5
insertion = len(s2) - 5
"""


def min_insertion_deletion_dp_bottom_up_tabular(s1, s2):
    n1, n2 = len(s1), len(s2)

    if n1 == 0 or n2 == 0:
        return -1

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for start in range(1, n1 + 1):
        for end in range(1, n2 + 1):
            if s1[start - 1] == s2[end - 1]:
                dp[start][end] = 1 + dp[start - 1][end - 1]
            else:
                dp[start][end] = max(dp[start][end - 1], dp[start - 1][end])

    count = dp[n1][n2]

    print("Min deletions needed :- ", len(s1) - count)
    print("Min insertions needed :- ", len(s2) - count)


print("========== min insertion and deletion dp bottom up ===========")
min_insertion_deletion_dp_bottom_up_tabular("abc", "fbc")
min_insertion_deletion_dp_bottom_up_tabular("abdca", "cbda")
min_insertion_deletion_dp_bottom_up_tabular("passport", "ppsspt")
