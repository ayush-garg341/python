"""
Given an infinite supply of ‘n’ coin denominations and a total money amount,
we are asked to find the total number of distinct ways to make up that amount.

explaination:
    example1:-
        Denominations: {1,2,3}
        Total amount: 5
        Output: 5
        Explanation: There are five ways to make the change for '5', here are those ways:
          1. {1,1,1,1,1}
          2. {1,1,1,2}
          3. {1,2,2}
          4. {1,1,3}
          5. {2,3}
"""


def count_change_recursive(denominations, total):
    return count_change_recursive_brute_force(denominations, total, 0)


def count_change_recursive_brute_force(
    denominations: list, total: int, current_idx: int
) -> int:
    if current_idx >= len(denominations):
        return 0

    if total == 0:
        return 1

    count = 0
    if denominations[current_idx] <= total:
        count += count_change_recursive_brute_force(
            denominations, total - denominations[current_idx], current_idx
        )

    count += count_change_recursive_brute_force(denominations, total, current_idx + 1)

    return count


print("================== brute force recursive ======================")
print(count_change_recursive([1, 2, 3], 5))
print(count_change_recursive([1, 2, 3], 4))
print(count_change_recursive([1, 2, 3], 3))


def count_change_dp(denominations, total):
    dp = [[0 for i in range(total + 1)] for j in range(len(denominations))]
    return count_change_dp_top_bottom(denominations, dp, total, 0)


def count_change_dp_top_bottom(
    denominations: list, dp: list, total: int, current_idx: int
):
    if current_idx >= len(denominations):
        return 0

    if total == 0:
        return 1

    if dp[current_idx][total] == 0:
        count = 0
        if denominations[current_idx] <= total:
            count += count_change_dp_top_bottom(
                denominations, dp, total - denominations[current_idx], current_idx
            )

        count += count_change_dp_top_bottom(denominations, dp, total, current_idx + 1)
        dp[current_idx][total] = count

    return dp[current_idx][total]


print("================== dp top bottom recursive ======================")
print(count_change_dp([1, 2, 3], 5))
print(count_change_dp([1, 2, 3], 4))
print(count_change_dp([1, 2, 3], 3))


def count_change_dp_tabular_bottom_up(denominations: list, total: int):
    n = len(denominations)
    if n == 0:
        return -1

    dp = [[0 for i in range(total + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for denom in range(1, total + 1):
            if denominations[i] <= denom:
                dp[i][denom] = dp[i][denom - denominations[i]]

            if i > 0:
                dp[i][denom] += dp[i - 1][denom]

    return dp[n - 1][total]


print("================== dp bottom up tabular ======================")
print(count_change_dp_tabular_bottom_up([1, 2, 3], 5))
print(count_change_dp_tabular_bottom_up([1, 2, 3], 4))
print(count_change_dp_tabular_bottom_up([1, 2, 3], 3))
