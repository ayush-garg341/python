"""
Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

Example 1:
    Input: string: “baxmx”, pattern: “ax”
    Output: 2
    Explanation: {baxmx, baxmx}.

Example 2:
    Input: string: “tomorrow”, pattern: “tor”
    Output: 4
    Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.
"""


def subseq_pattern_matching_brute_force(seq, pattern):
    return subseq_pattern_matching_brute_force_recursive(seq, pattern, 0, 0)


def subseq_pattern_matching_brute_force_recursive(
    seq: str, pattern: str, strIndex: int, patIndex: int
):
    if patIndex == len(pattern):
        return 1

    if strIndex == len(seq):
        return 0

    c1 = 0
    if seq[strIndex] == pattern[patIndex]:
        c1 = subseq_pattern_matching_brute_force_recursive(
            seq, pattern, strIndex + 1, patIndex + 1
        )

    c2 = subseq_pattern_matching_brute_force_recursive(
        seq, pattern, strIndex + 1, patIndex
    )

    return c1 + c2


print("======= subseq pattern matching count =======")
print(subseq_pattern_matching_brute_force("baxmx", "ax"))
print(subseq_pattern_matching_brute_force("tomorrow", "tor"))


def subseq_pattern_matching_dp_bottom_up(seq, pattern):
    seqLen, patLen = len(seq), len(pattern)

    if patLen == 0:
        return 1

    if patLen > seqLen:
        return 0

    dp = [[0 for _ in range(seqLen + 1)] for _ in range(patLen + 1)]

    for i in range(seqLen):
        dp[0][i] = 1

    for patIdx in range(1, patLen + 1):
        for strIdx in range(1, seqLen + 1):
            if seq[strIdx - 1] == pattern[patIdx - 1]:
                dp[patIdx][strIdx] = dp[patIdx - 1][strIdx - 1]
            dp[patIdx][strIdx] += dp[patIdx][strIdx - 1]
    return dp[patLen][seqLen]


print("======= subseq pattern matching count dp bottom up=======")
print(subseq_pattern_matching_dp_bottom_up("baxmx", "ax"))
print(subseq_pattern_matching_dp_bottom_up("tomorrow", "tor"))
