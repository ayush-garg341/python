"""
There are n houses built in a line. A thief wants to steal the maximum
possible money from these houses. The only restriction the thief has
is that he can’t steal from two consecutive houses, as that
would alert the security system. Maximize stealing ?

example1:
    Input: {2, 5, 1, 3, 6, 2, 4}
    Output: 15
    Explanation: The thief should steal from houses 5 + 6 + 4

example2:
    Input: {2, 10, 14, 8, 1}
    Output: 18
    Explanation: The thief should steal from houses 10 + 8
"""


def find_max_steal(wealth):
    max_wealth = find_max_steal_recursive(wealth, 0)
    return max_wealth


def find_max_steal_recursive(wealth: list, current_idx: int):
    n = len(wealth)
    if current_idx >= n:
        return 0

    max_steal1, max_steal2 = 0, 0
    max_steal1 += wealth[current_idx] + find_max_steal_recursive(
        wealth, current_idx + 2
    )

    max_steal2 += find_max_steal_recursive(wealth, current_idx + 1)

    return max(max_steal1, max_steal2)


print("======== find max steal brute force recursive ==========")
print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal([2, 10, 14, 8, 1]))
print(find_max_steal([20, 30, 40, 50, 60]))


def find_max_steal_dp_top_bottom(wealth):
    dp = [0 for i in range(len(wealth))]
    max_wealth = find_max_steal_dp_top_bottom_recursive(wealth, dp, 0)
    return max_wealth


def find_max_steal_dp_top_bottom_recursive(
    wealth: list, dp: list, current_idx: int
) -> int:
    if current_idx >= len(wealth):
        return 0

    if dp[current_idx] != 0:
        return dp[current_idx]

    max_steal1, max_steal2 = 0, 0
    max_steal1 += wealth[current_idx] + find_max_steal_recursive(
        wealth, current_idx + 2
    )

    max_steal2 += find_max_steal_recursive(wealth, current_idx + 1)
    dp[current_idx] = max(max_steal1, max_steal2)

    return dp[current_idx]


print("======== find max steal dp top bottom recursive ==========")
print(find_max_steal_dp_top_bottom([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal_dp_top_bottom([2, 10, 14, 8, 1]))
print(find_max_steal_dp_top_bottom([20, 30, 40, 50, 60]))


def find_max_steal_dp_bottom_up_tabular(wealth):
    n = len(wealth)
    if n == 0:
        return -1

    dp = [0 for i in range(len(wealth))]
    dp[0] = wealth[0]
    dp[1] = wealth[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + wealth[i])

    return dp[n - 1]


print("======== find max steal dp bottom up tabular ==========")
print(find_max_steal_dp_bottom_up_tabular([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal_dp_bottom_up_tabular([2, 10, 14, 8, 1]))
print(find_max_steal_dp_bottom_up_tabular([20, 30, 40, 50, 60]))
