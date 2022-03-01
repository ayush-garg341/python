"""
Given a sequence find the length of its LPS.
A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elts.

example1:
    Input: "abdbca"
    Output: 5
    Explanation: LPS is "abdba".

example2:
    Input: = "cddpd"
    Output: 3
    Explanation: LPS is "ddd".

example3:
    Input: = "pqr"
    Output: 1
    Explanation: LPS could be "p", "q" or "r".
"""


def find_lps_length(seq):
    n = len(seq)
    if n == 0:
        return -1

    start = 0
    end = len(seq) - 1

    count = find_lps_length_recursive(seq, start, end)
    return count


def find_lps_length_recursive(seq: str, start: int, end: int) -> int:
    if start == end:
        return 1
    if start > end:
        return 0

    print("start = {0}, end = {1}".format(start, end))
    count = 0
    if seq[start] == seq[end]:
        count += 2 + find_lps_length_recursive(seq, start + 1, end - 1)
    else:
        count1 = find_lps_length_recursive(seq, start + 1, end)
        count2 = find_lps_length_recursive(seq, start, end - 1)
        count += max(count1, count2)
    return count


print("======== find lps length brute force recusrive ==========")
print(find_lps_length("abdbca"))
print(find_lps_length("cddpd"))
print(find_lps_length("pqr"))


def find_lps_length_dp_top_bottom(seq):
    n = len(seq)
    if n == 0:
        return -1
    start = 0
    end = len(seq) - 1

    dp = [[-1 for i in range(len(seq))] for j in range(len(seq))]
    count = find_lps_length_dp_top_bottom_recursive(seq, dp, start, end)
    return count


def find_lps_length_dp_top_bottom_recursive(
    seq: str, dp: list, start: int, end: int
) -> int:
    if start == end:
        return 1
    if start > end:
        return 0

    if dp[start][end] == -1:
        print("start = {0}, end = {1}".format(start, end))
        if seq[start] == seq[end]:
            dp[start][end] = 2 + find_lps_length_dp_top_bottom_recursive(
                seq, dp, start + 1, end - 1
            )
        else:
            count1 = find_lps_length_dp_top_bottom_recursive(seq, dp, start + 1, end)
            count2 = find_lps_length_dp_top_bottom_recursive(seq, dp, start, end - 1)
            dp[start][end] = max(count1, count2)

    return dp[start][end]


print("======== find lps length dp top bottom recursive ==========")
print(find_lps_length_dp_top_bottom("abdbca"))
print(find_lps_length_dp_top_bottom("cddpd"))
print(find_lps_length_dp_top_bottom("pqr"))


def find_lps_length_dp_bottom_up_tabular(seq):
    n = len(seq)
    if n == 0:
        return -1

    dp = [[0 for i in range(len(seq))] for j in range(len(seq))]
    for i in range(len(seq)):
        dp[i][i] = 1

    for start in range(len(seq) - 2, -1, -1):
        for end in range(start + 1, n):
            if seq[start] == seq[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1]


print("======== find lps length dp bottom up tabular ==========")
print(find_lps_length_dp_bottom_up_tabular("abdbca"))
print(find_lps_length_dp_bottom_up_tabular("cddpd"))
print(find_lps_length_dp_bottom_up_tabular("pqr"))
