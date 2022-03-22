"""
LBS: A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

example1:
    Input: {4,2,3,6,10,1,12}
    Output: 5
    Explanation: The LBS is {2,3,6,10,1}.

example2:
    Input: {4,2,5,9,7,6,10,3,1}
    Output: 7
    Explanation: The LBS is {4,5,9,7,6,3,1}.

Approach:
    For every index ‘i’ in the given array, we will do two things:
    1. Find LDS starting from ‘i’ to the end of the array.
    2. Find LDS starting from ‘i’ to the beginning of the array.

LBS would be the maximum sum of the above two subsequences.
"""


def lbs_brute_force(seq: list) -> int:
    n = len(seq)
    if n < 3:
        return 0

    max_lbs = 0
    for i in range(1, n):
        lbs_left = longest_increasing_subseq(seq, 0, i)
        lbs_right = longest_increasing_subseq_rev(seq, n, i)
        max_lbs = max(lbs_left + lbs_right - 1, max_lbs)

    return max_lbs


def longest_increasing_subseq(seq, start, end):
    len_seq = end - start + 1
    dp = [1 for _ in range(len_seq)]

    for end in range(1, len_seq):
        for start in range(end):
            if seq[end] > seq[start]:
                dp[end] = max(dp[end], 1 + dp[start])
    return dp[end]


def longest_increasing_subseq_rev(seq, n, i):
    dp = [1 for _ in range(n)]

    for end in range(n - 1, i - 1, -1):
        for start in range(n - 1, end, -1):
            if seq[end] > seq[start]:
                dp[end] = max(dp[end], 1 + dp[start])

    return dp[i]


print(lbs_brute_force([4, 2, 3, 6, 10, 1, 12]))
print(lbs_brute_force([4, 2, 5, 9, 7, 6, 10, 3, 1]))


def longest_bitonic_seq_optimized(seq):
    n = len(seq)
    if n < 3:
        return 0

    lds = [1 for _ in range(n)]

    for end in range(1, n):
        for start in range(end):
            if seq[end] > seq[start]:
                lds[end] = max(1 + lds[start], lds[end])

    lds_rev = [1 for _ in range(n)]

    for end in range(n - 1, -1, -1):
        for start in range(n - 1, end, -1):
            if seq[end] > seq[start]:
                lds_rev[end] = max(lds_rev[end], 1 + lds_rev[start])

    max_bitonic = 0
    for i in range(n):
        max_bitonic = max(lds[i] + lds_rev[i] - 1, max_bitonic)

    return max_bitonic


print("===== optimized longest bitonic seq ======== ")
print(longest_bitonic_seq_optimized([4, 2, 3, 6, 10, 1, 12]))
print(longest_bitonic_seq_optimized([4, 2, 5, 9, 7, 6, 10, 3, 1]))
