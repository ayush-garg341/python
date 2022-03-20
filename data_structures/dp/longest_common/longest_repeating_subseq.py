"""
A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping.
i.e none of the corresponding characters in the repeating subsequences have the same index.

example1:
    input: tomorrow
    output: 2
    Explanation: The longest repeating subsequence is “or” {tomorrow}.

example2:
    input: aabdbcec
    output: 3
    Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

example3:
    input: fmff
    output: 2
    Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.
"""


def longest_repeating_subseq_brute_force(seq):
    return longest_repeating_subseq_brute_force_recursive(seq, 0, 0)


def longest_repeating_subseq_brute_force_recursive(seq: str, i: int, j: int):
    if i == len(seq) or j == len(seq):
        return 0

    if i != j and seq[i] == seq[j]:
        return 1 + longest_repeating_subseq_brute_force_recursive(seq, i + 1, j + 1)

    c1 = longest_repeating_subseq_brute_force_recursive(seq, i, j + 1)
    c2 = longest_repeating_subseq_brute_force_recursive(seq, i + 1, j)

    return max(c1, c2)


print("======== longest repeating subseq brute force ==========")
print(longest_repeating_subseq_brute_force("tomorrow"))
print(longest_repeating_subseq_brute_force("aabdbcec"))
print(longest_repeating_subseq_brute_force("fmfff"))


def longest_repeating_subseq_dp_top_bottom(seq):
    n = len(seq)
    if n == 0:
        return -1
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return longest_repeating_subseq_dp_top_bottom_recursive(seq, dp, 0, 0)


def longest_repeating_subseq_dp_top_bottom_recursive(
    seq: str, dp: list, i: int, j: int
):
    if i == len(seq) or j == len(seq):
        return 0

    if dp[i][j] == -1:
        if i != j and seq[i] == seq[j]:
            dp[i][j] = 1 + longest_repeating_subseq_dp_top_bottom_recursive(
                seq, dp, i + 1, j + 1
            )
        else:
            c1 = longest_repeating_subseq_dp_top_bottom_recursive(seq, dp, i, j + 1)
            c2 = longest_repeating_subseq_dp_top_bottom_recursive(seq, dp, i + 1, j)

            dp[i][j] = max(c1, c2)

    return dp[i][j]


print("======== longest repeating subseq dp top bottom =========")
print(longest_repeating_subseq_dp_top_bottom("tomorrow"))
print(longest_repeating_subseq_dp_top_bottom("aabdbcec"))
print(longest_repeating_subseq_dp_top_bottom("fmfff"))


def longest_repeating_subseq_dp_bottom_up(seq):
    n = len(seq)
    if n == 0:
        return -1

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if start != end and seq[start - 1] == seq[end - 1]:
                dp[start][end] = 1 + dp[start - 1][end - 1]
            else:
                dp[start][end] = max(dp[start - 1][end], dp[start][end - 1])

    return dp[n][n]


print("======== longest repeating subseq dp bottom up =========")
print(longest_repeating_subseq_dp_bottom_up("tomorrow"))
print(longest_repeating_subseq_dp_bottom_up("aabdbcec"))
print(longest_repeating_subseq_dp_bottom_up("fmfff"))
