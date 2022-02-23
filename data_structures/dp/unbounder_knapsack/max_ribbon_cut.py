"""
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths.
We need to cut the ribbon into the maximum number of pieces that comply with
the above-mentioned possible lengths.

example1:-
    n: 5
    Ribbon Lengths: {2,3,5}
    Output: 2
    Explanation: Ribbon pieces will be {2,3}.

example2:
    n: 7
    Ribbon Lengths: {2,3}
    Output: 3
    Explanation: Ribbon pieces will be {2,2,3}.
"""


import math


def count_ribbon_pieces(ribbonLengths, total):
    max_change = count_ribbon_pieces_recursive(ribbonLengths, total, 0)
    return max_change if max_change != -math.inf else -1


def count_ribbon_pieces_recursive(ribbonLengths: list, total: int, current_idx: int):
    if total == 0:
        return 0
    if current_idx >= len(ribbonLengths):
        return -math.inf

    count1 = -math.inf
    if ribbonLengths[current_idx] <= total:
        res = count_ribbon_pieces_recursive(
            ribbonLengths, total - ribbonLengths[current_idx], current_idx
        )
        if res != -math.inf:
            count1 = 1 + res

    count2 = count_ribbon_pieces_recursive(ribbonLengths, total, current_idx + 1)

    return max(count1, count2)


print("======== count ribbon pieces brute force recusrive ========")
print(count_ribbon_pieces([2, 3, 5], 5))
print(count_ribbon_pieces([2, 3], 7))
print(count_ribbon_pieces([3, 5, 7], 13))
print(count_ribbon_pieces([3, 5], 7))


def count_ribbon_pieces_dp_top_bottom(ribbonLengths, total):
    dp = [[-math.inf for i in range(total + 1)] for j in range(len(ribbonLengths))]
    max_change = count_ribbon_pieces_dp_top_bottom_recursive(
        ribbonLengths, dp, total, 0
    )
    return max_change if max_change != -math.inf else -1


def count_ribbon_pieces_dp_top_bottom_recursive(
    ribbonLengths: list, dp: list, total: int, current_idx: int
):
    if total == 0:
        return 0
    if current_idx >= len(ribbonLengths):
        return -math.inf

    if dp[current_idx][total] == -math.inf:
        count1 = -math.inf
        if ribbonLengths[current_idx] <= total:
            res = count_ribbon_pieces_dp_top_bottom_recursive(
                ribbonLengths, dp, total - ribbonLengths[current_idx], current_idx
            )
            if res != -math.inf:
                count1 = 1 + res

        count2 = count_ribbon_pieces_dp_top_bottom_recursive(
            ribbonLengths, dp, total, current_idx + 1
        )

        dp[current_idx][total] = max(count1, count2)

    return dp[current_idx][total]


print("======== count ribbon pieces dp top bottom ========")
print(count_ribbon_pieces_dp_top_bottom([2, 3, 5], 5))
print(count_ribbon_pieces_dp_top_bottom([2, 3], 7))
print(count_ribbon_pieces_dp_top_bottom([3, 5, 7], 13))
print(count_ribbon_pieces_dp_top_bottom([3, 5], 7))


def max_ribbon_pieces_bottom_up_tabular(ribbonLengths, total):
    n = len(ribbonLengths)
    if n == 0:
        return -1

    dp = [[-math.inf for i in range(total + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for lent in range(1, total + 1):

            if lent >= ribbonLengths[i]:
                if dp[i][lent - ribbonLengths[i]] != -math.inf:
                    dp[i][lent] = 1 + dp[i][lent - ribbonLengths[i]]

            if i > 0:
                dp[i][lent] = max(dp[i][lent], dp[i - 1][lent])

    return -1 if dp[n - 1][total] == -math.inf else dp[n - 1][total]


print("============ max ribbon piece count bottom up tabular =========")
print(max_ribbon_pieces_bottom_up_tabular([2, 3, 5], 5))
print(max_ribbon_pieces_bottom_up_tabular([2, 3], 7))
print(max_ribbon_pieces_bottom_up_tabular([3, 5, 7], 13))
print(max_ribbon_pieces_bottom_up_tabular([3, 5], 7))
