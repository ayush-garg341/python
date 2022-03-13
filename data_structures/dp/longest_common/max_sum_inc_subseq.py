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
