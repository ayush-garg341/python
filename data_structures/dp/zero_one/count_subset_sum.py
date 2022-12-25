"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

example-1:
    Input: {1, 1, 2, 3}, S=4
    Output: 3
    The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
    Note that we have two similar sets {1, 3}, because we have two '1' in our input.

example-2:
    Input: {1, 2, 7, 1, 5}, S=9
    Output: 3
    The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
"""


def count_subset_sum(arr, s):
    count = 0
    current_idx = 0
    count = count_subset_sum_brute_force(arr, current_idx, s)
    return count


def count_subset_sum_brute_force(arr: list, current_idx: int, s: int) -> int:
    if s == 0:
        return 1
    if current_idx >= len(arr):
        return 0

    count = 0
    if arr[current_idx] <= s:
        count += count_subset_sum_brute_force(
            arr, current_idx + 1, s - arr[current_idx]
        )

    count += count_subset_sum_brute_force(arr, current_idx + 1, s)

    return count


print("=============== brute force recursive ===============")
print(count_subset_sum([1, 1, 2, 3], 4))
print(count_subset_sum([1, 2, 7, 1, 5], 9))
print(count_subset_sum([1, 2, 3], 4))


def count_subset_sum_dp(arr, s):
    count = 0
    current_idx = 0
    dp = [[-1 for i in range(s + 1)] for j in range(len(arr))]
    count = count_subset_sum_dp_top_bottom(arr, current_idx, s, dp)
    return count


def count_subset_sum_dp_top_bottom(
    arr: list, current_idx: int, s: int, dp: list
) -> int:
    if s == 0:
        return 1
    if current_idx >= len(arr):
        return 0

    if dp[current_idx][s] == -1:
        count = 0
        if arr[current_idx] <= s:
            count += count_subset_sum_brute_force(
                arr, current_idx + 1, s - arr[current_idx]
            )

        count += count_subset_sum_brute_force(arr, current_idx + 1, s)
        dp[current_idx][s] = count

    return dp[current_idx][s]


print("=============== top bottom dp recursive ===============")
print(count_subset_sum_dp([1, 1, 2, 3], 4))
print(count_subset_sum_dp([1, 2, 7, 1, 5], 9))
print(count_subset_sum_dp([1, 2, 3], 4))


def count_subset_sum_dp_bottom_up_tabular(arr: list, s: int) -> int:
    n = len(arr)
    if n == 0:
        return 0

    dp = [[0 for i in range(s + 1)] for j in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1

    for s in range(1, s + 1):
        if s == arr[0]:
            dp[0][s] = 1

    for i in range(1, len(arr)):
        for s in range(1, s + 1):
            count1, count2 = 0, 0
            count1 = dp[i - 1][s]
            if arr[i] <= s:
                count2 = dp[i - 1][s - arr[i]]

            dp[i][s] = count1 + count2

    return dp[n - 1][s]


print("=============== bottom up tabular ===============")
print(count_subset_sum_dp_bottom_up_tabular([1, 1, 2, 3], 4))
print(count_subset_sum_dp_bottom_up_tabular([1, 2, 7, 1, 5], 9))
print(count_subset_sum_dp_bottom_up_tabular([1, 2, 3], 4))
