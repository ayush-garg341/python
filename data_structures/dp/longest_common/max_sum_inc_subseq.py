"""
Given a number sequence, find the increasing subsequence with the highest sum.

example1:
    Input: {4,1,2,6,10,1,12}
    Output: 32
    Explanation: The increaseing sequence is {4,6,10,12}.
    Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.

example2:
    Input: {-4,10,3,7,15}
    Output: 25
    Explanation: The increaseing sequences are {10, 15} and {3,7,15}.
"""

import math


def max_sum_inc_subseq_brute_force(seq):
    prev = -1
    curr = 0
    return max_sum_inc_subseq_brute_force_recursive(seq, prev, curr)


def max_sum_inc_subseq_brute_force_recursive(seq: list, prev: int, curr: int):
    if prev == curr or curr == len(seq):
        return 0

    sum1, sum2 = 0, 0
    if prev == -1 or seq[curr] > seq[prev]:
        sum1 = seq[curr] + max_sum_inc_subseq_brute_force_recursive(seq, curr, curr + 1)
    sum2 = max_sum_inc_subseq_brute_force_recursive(seq, prev, curr + 1)
    return max(sum1, sum2)


print("====== max sum for increasing subseq brute force recursive ======")
print(max_sum_inc_subseq_brute_force([4, 1, 2, 6, 10, 1, 12]))
print(max_sum_inc_subseq_brute_force([-4, 10, 3, 7, 15]))


def max_sum_inc_subseq_dp_top_bottom(seq):
    dp = [[-math.inf for _ in range(len(seq))] for _ in range(len(seq))]
    prev = -1
    curr = 0
    return max_sum_inc_subseq_dp_top_bottom_recursive(seq, dp, prev, curr)


def max_sum_inc_subseq_dp_top_bottom_recursive(
    seq: list, dp: list, prev: int, curr: int
):
    if prev == curr or curr == len(seq):
        return 0

    if dp[prev + 1][curr] == -math.inf:
        sum1, sum2 = 0, 0
        if prev == -1 or seq[curr] > seq[prev]:
            sum1 = seq[curr] + max_sum_inc_subseq_dp_top_bottom_recursive(
                seq, dp, curr, curr + 1
            )
        sum2 = max_sum_inc_subseq_dp_top_bottom_recursive(seq, dp, prev, curr + 1)
        dp[prev + 1][curr] = max(sum1, sum2)
    return dp[prev + 1][curr]


print("====== max sum for increasing subseq dp top bottom recursive ======")
print(max_sum_inc_subseq_dp_top_bottom([4, 1, 2, 6, 10, 1, 12]))
print(max_sum_inc_subseq_dp_top_bottom([-4, 10, 3, 7, 15]))


def max_sum_inc_subseq_dp_bottom_up_tabular(seq):
    n = len(seq)
    if n == 0:
        return -1

    dp = [seq[i] for i in range(n)]

    max_sum = -math.inf
    for start in range(1, n):
        for end in range(0, start):
            if seq[start] > seq[end]:
                dp[start] = max(dp[start], seq[start] + dp[end])
                max_sum = max(max_sum, dp[start])

    print(dp)
    return max_sum


print("====== max sum for increasing subseq dp bottom up tabular ======")
print(max_sum_inc_subseq_dp_bottom_up_tabular([4, 1, 2, 6, 10, 1, 12]))
print(max_sum_inc_subseq_dp_bottom_up_tabular([-4, 10, 3, 7, 15]))
