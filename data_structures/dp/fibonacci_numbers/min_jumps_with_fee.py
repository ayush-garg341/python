"""
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing
the fee that you have to pay if you take the step. Implement a method to
calculate the minimum fee required to reach the top of the staircase
(beyond the top-most step, beyond the last element).
At every step, you have an option to take either 1 step, 2 steps, or 3 steps.

example1:
    Number of stairs (n) : 6
    Fee: {1,2,5,2,1,2}
    Output: 3
    Explanation: Starting from index '0', we reach the top through: 0->3->top
    The total fee we have to pay will be (1+2).

example2:
    Number of stairs (n): 4
    Fee: {2,3,4,5}
    Output: 5
    Explanation: Starting from index '0', we reach the top through: 0->1->top
    The total fee we have to pay will be (2+3).
"""

import math


def find_min_fee(fee):
    min_fee = find_min_fee_recursive(fee, 0)
    return min_fee if min_fee != math.inf else -1


def find_min_fee_recursive(fee: list, current_idx: int):
    n = len(fee)
    if current_idx > n - 1:
        return 0

    start = current_idx + 1
    end = current_idx + 3
    min_fee = math.inf
    print("calculating for n = ", current_idx)
    while start <= end and start <= len(fee):
        current_fee = find_min_fee_recursive(fee, start)
        start += 1
        if current_fee != math.inf:
            min_fee = min(min_fee, current_fee + fee[current_idx])

    return min_fee


print("======= find min fee recursive brute force ==========")
print(find_min_fee([1, 2, 5, 2, 1, 3]))
print(find_min_fee([2, 3, 4, 5]))


def find_min_fee_top_bottom(fee):
    dp = [0 for i in range(len(fee))]
    min_fee = find_min_fee_top_bottom_recursive(fee, dp, 0)
    return min_fee if min_fee != math.inf else -1


def find_min_fee_top_bottom_recursive(fee: list, dp: list, current_idx: int):
    n = len(fee)
    if current_idx > n - 1:
        return 0

    if dp[current_idx] == 0:
        print("calculating for n = ", current_idx)
        take1step = find_min_fee_top_bottom_recursive(fee, dp, current_idx + 1)
        take2step = find_min_fee_top_bottom_recursive(fee, dp, current_idx + 2)
        take3step = find_min_fee_top_bottom_recursive(fee, dp, current_idx + 3)
        _min = min(take1step, take2step, take3step)
        dp[current_idx] = _min + fee[current_idx]
    return dp[current_idx]


print("======= find min fee dp top bottom recursive ==========")
print(find_min_fee_top_bottom([1, 2, 5, 2, 1, 3]))
print(find_min_fee_top_bottom([2, 3, 4, 5]))


def find_min_fee_dp_bottom_up_tabular(fee):
    n = len(fee)
    if n == 0:
        return -1

    dp = [0 for i in range(len(fee) + 1)]
    dp[0] = 0
    dp[1] = fee[0]
    dp[2] = fee[0]

    for start in range(2, n):
        dp[start + 1] = min(
            dp[start - 0] + fee[start - 0],
            dp[start - 1] + fee[start - 1],
            dp[start - 2] + fee[start - 2],
        )

    return dp[n]


print("======= find min fee dp bottom up tabular ==========")
print(find_min_fee_dp_bottom_up_tabular([1, 2, 5, 2, 1, 3]))
print(find_min_fee_dp_bottom_up_tabular([2, 3, 4, 5]))
