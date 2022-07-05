"""
Write a function that takes in two strings and returns the minimum number of edit operations.
Edit ops includes -> insertion, deletion, and replacement

example1:
    str1 = "abc"
    str2 = "yabd"
    edit distance = 2 (one for insertion of "y" and other replacing "c" with "d")

"""


def levenshteinDistance(str1, str2):
    # Write your code here.
    n2 = len(str2)
    n1 = len(str1)
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]

    # Handles the case when len(str1) == 0
    for i in range(n2 + 1):
        dp[0][i] = i

    # Handles the case when len(str2) == 0
    for j in range(n1 + 1):
        dp[j][0] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))

    return dp[n1][n2]


print(levenshteinDistance("yabd", "abc"))


def lev_distance(str1, str2):

    return lev_distance_rec(str1, str2, 0, 0)


def lev_distance_rec(str1, str2, str1_index, str2_index):
    if len(str1) == str1_index:
        return len(str2) - str2_index

    if len(str2) == str2_index:
        return len(str1) - str1_index

    if str1[str1_index] == str2[str2_index]:
        return lev_distance_rec(str1, str2, str1_index + 1, str2_index + 1)

    # for delete
    delete = 1 + lev_distance_rec(str1, str2, str1_index + 1, str2_index)

    # for insert
    insert = 1 + lev_distance_rec(str1, str2, str1_index, str2_index + 1)

    # for replace
    replace = 1 + lev_distance_rec(str1, str2, str1_index + 1, str2_index + 1)

    return min(insert, min(delete, replace))


print(lev_distance("yabc", "abd"))
