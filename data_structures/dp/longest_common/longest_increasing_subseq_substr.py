"""
Given a number sequence, find the length of its Longest Increasing Subsequence (LIS).
In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

example1:
    Input: {4,2,3,6,10,1,12}
    Output: 5
    Explanation: The LIS is {2,3,6,10,12}.

example2:
    Input: {-4,10,3,7,15}
    Output: 4
    Explanation: The LIS is {-4,3,7,15}.
"""


def longest_increasing_substr_naive(seq):
    n = len(seq)
    if n == 0:
        return -1

    max_count = 0
    for start in range(n):
        count = 1
        index = start
        for end in range(start + 1, n):
            if seq[end] > seq[index]:
                index = end
                count += 1
            else:
                break
        max_count = max(max_count, count)

    return max_count


print("====== longest increasing substring naive ========")
print(longest_increasing_substr_naive([4, 2, 3, 6, 10, 1, 12]))
print(longest_increasing_substr_naive([-4, 10, 3, 7, 15]))


def longest_increasing_subseq_dp_bottom_up_tabular(seq):
    n = len(seq)
    if n == 0:
        return -1

    dp = [1 for _ in range(n)]

    max_count = 1
    for start in range(1, n):
        for end in range(0, start):
            if seq[start] > seq[end]:
                dp[start] = max(dp[start], 1 + dp[end])
                max_count = max(max_count, dp[start])

    return max_count


print("====== longest increasing subseq dp bottom up tabular ========")
print(longest_increasing_subseq_dp_bottom_up_tabular([4, 2, 3, 6, 10, 1, 12]))
print(longest_increasing_subseq_dp_bottom_up_tabular([-4, 10, 3, 7, 15]))
print(longest_increasing_subseq_dp_bottom_up_tabular([8, 9, 9, 10, 12, 21, 20]))
