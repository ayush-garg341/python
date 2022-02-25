"""
Given an array of positive numbers, where each element represents the max
number of jumps that can be made forward from that element, write a program
to find the minimum number of jumps needed to reach the end of the array
(starting from the first element). If an element is 0,
then we cannot move through that element.

example1:-
    Input = {2,1,1,1,4}
    Output = 3
    Explanation: Starting from index '0', we can reach the last index through:
                 0->2->3->4

example2:-
    Input = {1,1,3,6,9,3,0,1,3}
    Output = 4
    Explanation: Starting from index '0', we can reach the last index through: 
                 0->1->2->3->8
"""

import math


def count_min_jumps(jumps):
    count = count_min_jumps_recursive(jumps, 0)
    return count if count != math.inf else -1


def count_min_jumps_recursive(jumps, current_idx):
    if current_idx >= len(jumps) - 1:
        return 0

    if jumps[current_idx] == 0:
        return math.inf

    start = current_idx + 1
    end = current_idx + jumps[current_idx]
    count = math.inf
    while start <= end and start < len(jumps):
        min_jump = count_min_jumps_recursive(jumps, start)
        start += 1
        if min_jump != math.inf:
            count = min(count, min_jump + 1)

    return count


print("======== count min jumps brute force ==========")
print(count_min_jumps([2, 1, 1, 1, 4]))
print(count_min_jumps([1, 2, 6, 2, 9, 3, 0, 1, 3]))
print(count_min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(count_min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(count_min_jumps([3, 0, 8, 2, 0, 0, 1]))
print(count_min_jumps([0, 0, 0, 0]))


def count_min_jumps_dp_top_bottom(jumps):
    dp = [math.inf for i in range(len(jumps))]
    count = count_min_jumps_dp_top_bottom_recursive(jumps, dp, 0)
    return count if count != math.inf else -1


def count_min_jumps_dp_top_bottom_recursive(
    jumps: list, dp: list, current_idx: int
) -> float:
    if current_idx >= len(jumps) - 1:
        return 0

    if jumps[current_idx] == 0:
        return math.inf

    if dp[current_idx] == math.inf:
        start = current_idx + 1
        end = current_idx + jumps[current_idx]
        count = math.inf
        while start <= end and start < len(jumps):
            min_jumps = count_min_jumps_dp_top_bottom_recursive(jumps, dp, start)
            start += 1
            if min_jumps != math.inf:
                count = min(count, min_jumps + 1)
                dp[current_idx] = count

    return dp[current_idx]


print("======== count min jumps dp top bottom recursive ==========")
print(count_min_jumps_dp_top_bottom([2, 1, 1, 1, 4]))
print(count_min_jumps_dp_top_bottom([1, 2, 6, 2, 9, 3, 0, 1, 3]))
print(count_min_jumps_dp_top_bottom([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(count_min_jumps_dp_top_bottom([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(count_min_jumps_dp_top_bottom([3, 0, 8, 2, 0, 0, 1]))
print(count_min_jumps_dp_top_bottom([0, 0, 0, 0]))


def count_min_jumps_dp_tabular_bottom_up(jumps):
    n = len(jumps)
    dp = [math.inf for i in range(n)]
    dp[0] = 0

    for start in range(n - 1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], dp[start] + 1)
            end += 1
    return dp[n - 1] if dp[n - 1] != math.inf else -1


print("======== count min jumps dp bottom up tabular ==========")
print(count_min_jumps_dp_tabular_bottom_up([2, 1, 1, 1, 4]))
print(count_min_jumps_dp_tabular_bottom_up([1, 2, 6, 2, 9, 3, 0, 1, 3]))
print(count_min_jumps_dp_tabular_bottom_up([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(count_min_jumps_dp_tabular_bottom_up([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(count_min_jumps_dp_tabular_bottom_up([3, 0, 8, 2, 0, 0, 1]))
print(count_min_jumps_dp_tabular_bottom_up([0, 0, 0, 0]))
