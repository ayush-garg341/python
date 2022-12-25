"""
Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
ex.1
    i/p - {1, 2, 3, 7}, S=6
    o/p - True
    exp - The given set has a subset whose sum is '6': {1, 2, 3}
ex.2
    i/p - {1, 2, 7, 1, 5}, S=10
    o/p - True
    exp - The given set has a subset whose sum is '10': {1, 2, 7}
"""


def is_subset_exist(arr, s):
    exist = False
    current_idx = 0
    exist = is_subset_exist_recursive_brute_force(arr, s, current_idx)
    return exist


def is_subset_exist_recursive_brute_force(arr: list, s: int, current_idx: int) -> bool:
    if s == 0:
        return True
    if current_idx >= len(arr):
        return False

    if arr[current_idx] <= s:
        if is_subset_exist_recursive_brute_force(
            arr, s - arr[current_idx], current_idx + 1
        ):
            return True

    return is_subset_exist_recursive_brute_force(arr, s, current_idx + 1)


print("============recursive brute force===============")
print(is_subset_exist([1, 2, 3, 7], 6))
print(is_subset_exist([1, 2, 7, 1, 5], 10))
print(is_subset_exist([1, 3, 4, 8], 6))


def is_subset_exist_top_bottom(arr, s):
    exist = False
    dp = [[-1 for i in range(0, s + 1)] for j in range(0, len(arr))]
    current_idx = 0
    exist = is_subset_exist_top_bottom_dp(arr, s, current_idx, dp)
    if exist == 1:
        return True
    return False


def is_subset_exist_top_bottom_dp(arr: list, s: int, current_idx: int, dp: list) -> int:
    if s == 0:
        return 1
    if current_idx >= len(arr):
        return 0

    if dp[current_idx][s] == -1:
        if arr[current_idx] <= s:
            if (
                is_subset_exist_top_bottom_dp(
                    arr, s - arr[current_idx], current_idx + 1, dp
                )
                == 1
            ):
                dp[current_idx][s] = 1
                return dp[current_idx][s]
        dp[current_idx][s] = is_subset_exist_top_bottom_dp(arr, s, current_idx + 1, dp)

    return dp[current_idx][s]


print("============dp solution top bottoms=============")
print(is_subset_exist_top_bottom([1, 2, 3, 7], 6))
print(is_subset_exist_top_bottom([1, 2, 7, 1, 5], 10))
print(is_subset_exist_top_bottom([1, 3, 4, 8], 6))
print(is_subset_exist_top_bottom([1, 3, 6], 6))


def is_subset_exist_bottom_up(arr, s):
    n = len(arr)
    if n == 0:
        return False

    dp = [[0 for i in range(s + 1)] for j in range(0, len(arr))]

    for i in range(s + 1):
        if arr[0] >= i:
            dp[0][i] = 1

    for i in range(len(arr)):
        dp[i][0] = 1

    for i in range(1, len(arr)):
        for s in range(s + 1):
            if dp[i - 1][s] == 1:
                dp[i][s] = 1
            elif arr[i] <= s:
                dp[i][s] = dp[i - 1][s - arr[i]]

    if dp[n - 1][s] == 1:
        return True

    return False


print("============dp solution bottom up=============")
print(is_subset_exist_bottom_up([1, 2, 3, 7], 6))
print(is_subset_exist_bottom_up([1, 2, 7, 1, 5], 10))
print(is_subset_exist_bottom_up([1, 3, 4, 8], 6))
print(is_subset_exist_bottom_up([1, 3, 6], 6))
