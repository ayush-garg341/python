"""
Given a number sequence, find the minimum number of elements
that should be deleted to make the remaining sequence sorted.

example1:
    Input: {4,2,3,6,10,1,12}
    Output: 2
    Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.

example2:
    Input: {-4,10,3,7,15}
    Output: 1
    Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.

example3:
    Input: {3,2,1,0}
    Output: 3
    Explanation: Since the elements are in reverse order, we have to delete all except one to get a
    sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

Approach:
    We can calculate the LIS and subtract LIS from length of sequence.
"""


def min_deletions_to_make_seq_sorted(seq):
    n = len(seq)
    if n == 0:
        return -1

    dp = [1 for _ in range(n)]

    max_count = 1
    for end in range(1, n):
        for start in range(0, end):
            if seq[end] > seq[start]:
                dp[end] = max(dp[end], 1 + dp[start])
                max_count = max(dp[end], max_count)

    return n - max_count


print("======== min deletions to make seq sorted dp bottom up tabular =======")
print(min_deletions_to_make_seq_sorted([-4, 10, 3, 7, 15]))
print(min_deletions_to_make_seq_sorted([4, 3, 2, 1, 0]))
