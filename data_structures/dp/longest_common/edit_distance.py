"""
Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters.
Write a function to calculate the count of the minimum number of edit operations.

example1:
    Input: s1 = "bat"
           s2 = "but"
    Output: 1
    Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.

example2:
    Input: s1 = "abdca"
           s2 = "cbda"
    Output: 2
    Explanation: We can replace first 'a' with 'c' and delete second 'c'.

example3:
    Input: s1 = "passpot"
           s2 = "ppsspqrt"
    Output: 3
    Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.
"""


def brute_force_max_edit_distance(str1, str2):
    return brute_force_max_edit_distance_recursive(str1, str2, 0, 0)


def brute_force_max_edit_distance_recursive(str1: str, str2: str, str1_index: int, str2_index: int):
    if str1_index == len(str1):
        return len(str2) - str2_index

    if str2_index == len(str2):
        return len(str1) - str1_index

    if str1[str1_index] == str2[str2_index]:
        return brute_force_max_edit_distance_recursive(str1, str2, str1_index + 1, str2_index + 1)

    l1 = 1 + brute_force_max_edit_distance_recursive(str1, str2, str1_index + 1, str2_index)  # delete
    l2 = 1 + brute_force_max_edit_distance_recursive(str1, str2, str1_index, str2_index + 1)  # insert
    l3 = 1 + brute_force_max_edit_distance_recursive(str1, str2, str1_index + 1, str2_index + 1)  # replace

    return min(l1, min(l2, l3))


print("======== brute force max edit distance ========")
print(brute_force_max_edit_distance("bat", "but"))
print(brute_force_max_edit_distance("abdca", "cbda"))
print(brute_force_max_edit_distance("passpot", "ppsspqrt"))


def max_edit_distance_dp_bottom_up(str1, str2):
    n1, n2 = len(str1), len(str2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # if s1 is empty
    for i in range(n2 + 1):
        dp[0][i] = i

    # if s2 is empty
    for i in range(n1 + 1):
        dp[i][0] = i

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))

    return dp[n1][n2]


print("======== dp max edit distance bottom up ========")
print(max_edit_distance_dp_bottom_up("bat", "but"))
print(max_edit_distance_dp_bottom_up("abdca", "cbda"))
print(max_edit_distance_dp_bottom_up("passpot", "ppsspqrt"))
print(max_edit_distance_dp_bottom_up("pa", "ppss"))
