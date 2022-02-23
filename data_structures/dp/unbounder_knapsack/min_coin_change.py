"""
Given an infinite supply of ‘n’ coin denominations and a total money amount,
we are asked to find the minimum number of coins needed to make up that amount.

example1:
    Denominations: {1,2,3}
    Total amount: 5
    Output: 2
    Explanation: We need a minimum of two coins {2,3} to make a total of '5'

example2:
    Denominations: {1,2,3}
    Total amount: 11
    Output: 4
    Explanation: We need a minimum of four coins {2,3,3,3} to make a total of 11
"""

import math


def min_coin_change_brute_force(denominations, total):
    min_change = min_coin_change_brute_force_recursive(denominations, total, 0)
    return min_change if min_change != math.inf else -1


def min_coin_change_brute_force_recursive(
    denominations: list, total: int, current_idx: int
):

    if total == 0:
        return 0
    if current_idx >= len(denominations):
        return math.inf

    count1 = math.inf
    if total >= denominations[current_idx]:
        res = min_coin_change_brute_force_recursive(
            denominations, total - denominations[current_idx], current_idx
        )
        if res != math.inf:
            count1 = 1 + res

    count2 = min_coin_change_brute_force_recursive(
        denominations, total, current_idx + 1
    )

    return min(count1, count2)


print("==================== recursive brute force ==================")
print(min_coin_change_brute_force([1, 2, 3], 5))
print(min_coin_change_brute_force([1, 2, 3], 11))
print(min_coin_change_brute_force([1, 2, 3], 7))
print(min_coin_change_brute_force([3, 5], 7))


def min_coin_change_dp_top_bottom(denominations, total):
    n = len(denominations)
    if n == 0:
        return -1
    dp = [[math.inf for i in range(total + 1)] for j in range(len(denominations))]
    min_change = min_coin_change_dp_top_bottom_recursive(denominations, dp, total, 0)
    return min_change if min_change != math.inf else -1


def min_coin_change_dp_top_bottom_recursive(
    denominations: list, dp: list, total: int, current_idx: int
):

    if total == 0:
        return 0
    if current_idx >= len(denominations):
        return math.inf

    if dp[current_idx][total] == math.inf:
        count1 = math.inf
        if total >= denominations[current_idx]:
            res = min_coin_change_dp_top_bottom_recursive(
                denominations, dp, total - denominations[current_idx], current_idx
            )
            if res != math.inf:
                count1 = 1 + res

        count2 = min_coin_change_brute_force_recursive(
            denominations, total, current_idx + 1
        )

        dp[current_idx][total] = min(count1, count2)

    return dp[current_idx][total]


print("==================== dp top bottom recursive ==================")
print(min_coin_change_dp_top_bottom([1, 2, 3], 5))
print(min_coin_change_dp_top_bottom([1, 2, 3], 11))
print(min_coin_change_dp_top_bottom([1, 2, 3], 7))
print(min_coin_change_dp_top_bottom([3, 5], 7))


def min_coin_change_dp_bottom_up_tabular(denominations: list, total: int):
    n = len(denominations)

    if n == 0:
        return -1

    dp = [[0 for i in range(total + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for denom in range(1, total + 1):
            count1, count2 = 0, 0

            if denom >= denominations[i]:
                if dp[i][denom - denominations[i]] > 0 or denom % denominations[i] == 0:
                    count1 = 1 + dp[i][denom - denominations[i]]
            if i > 0:
                count2 = dp[i - 1][denom]

            if i == 0:
                dp[i][denom] = count1
            elif count1 != 0 and count2 != 0:
                dp[i][denom] = min(count1, count2)
            elif count1 != 0:
                dp[i][denom] = count1
            else:
                dp[i][denom] = count2

    return dp[n - 1][total] if dp[n - 1][total] != 0 else -1


print("==================== dp bottom up tabular ==================")
print(min_coin_change_dp_bottom_up_tabular([1, 2, 3], 5))
print(min_coin_change_dp_bottom_up_tabular([1, 2, 3], 11))
print(min_coin_change_dp_bottom_up_tabular([1, 2, 3], 7))
print(min_coin_change_dp_bottom_up_tabular([3, 5], 7))
