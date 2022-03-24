"""
Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
A subsequence is considered alternating if its elements are in alternating order.

A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:
{a1 > a2 < a3 } or { a1 < a2 > a3}.

example1:
    Input: {1,2,3,4}
    Output: 2
    Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}

example2:
    Input: {3,2,1,4}
    Output: 3
    Explanation: The LAS are {3,2,4} and {2,1,4}.

example3:
    Input: {1,3,2,4}
    Output: 4
    Explanation: The LAS is {1,3,2,4}.

Approach:
Try finding the LAS starting from every number in both ascending and descending order. So for every index ‘i’ in the
given array, we will have three options:
    1. If the element at ‘i’ is bigger than the last element we considered, we include the element at ‘i’ and recursively
    process the remaining array to find the next element in descending order.
    2. If the element at ‘i’ is smaller than the last element we considered, we include the element at ‘i’ and recursively
    process the remaining array to find the next element in ascending order.
    3. In addition to the above two cases, we can always skip the element ‘i’ to recurse for the remaining array.
    This will ensure that we try all subsequences.

"""


def brute_force_las(seq):
    n = len(seq)
    if n <= 2:
        return 0
    return max(brute_force_las_recursive(seq, -1, 0, True), brute_force_las_recursive(seq, -1, 0, False))


def brute_force_las_recursive(seq: list, prev: int, curr: int, flag: bool):
    if curr == len(seq):
        return 0

    c1 = 0
    if flag:
        if prev == -1 or seq[curr] > seq[prev]:
            c1 = 1 + brute_force_las_recursive(seq, curr, curr + 1, not flag)
    else:
        if prev == -1 or seq[curr] < seq[prev]:
            c1 += 1 + brute_force_las_recursive(seq, curr, curr + 1, not flag)

    c2 = brute_force_las_recursive(seq, prev, curr + 1, flag)

    return max(c1, c2)


print("====== brute force recursive las =======")
print(brute_force_las([1, 3, 2, 4]))
print(brute_force_las([3, 2, 1, 4]))
print(brute_force_las([1, 2, 3, 4]))


def brute_force_bottom_up_dp(seq):
    n = len(seq)
    if n == 0:
        return 0

    dp = [[0 for _ in range(2)] for i in range(n)]

    max_len = 1
    for i in range(n):
        dp[i][0] = dp[i][1] = 1

        for j in range(i):
            if seq[i] > seq[j]:
                dp[i][0] = max(dp[j][1] + 1, dp[i][0])
                max_len = max(max_len, dp[i][0])
            elif seq[i] != seq[j]:
                dp[i][1] = max(dp[j][0] + 1, dp[i][1])
                max_len = max(max_len, dp[i][1])

    return max_len


print("====== dp bottom up las =======")
print(brute_force_bottom_up_dp([1, 3, 2, 4]))
print(brute_force_bottom_up_dp([3, 2, 1, 4]))
print(brute_force_bottom_up_dp([1, 2, 3, 4]))
