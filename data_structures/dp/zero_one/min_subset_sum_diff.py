"""
Given a set of positive numbers, partition the set into two subsets with a
minimum difference between their subset sums.

example-1.
    Input: {1, 2, 3, 9}
    Output: 3
    Explanation: We can partition the given set into two subsets where the minimum absolute difference
        between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

example-2.
    Input: {1, 2, 7, 1, 5}
    Output: 0
    Explanation: We can partition the given set into two subsets where the minimum absolute difference
        between the sum of numbers is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
"""


import math

def min_subset_sum_diff(arr: list):
    s = sum(arr)
    find = 0
    if s%2 == 0:
        find = int(s/2)
    else:
        find = math.floor(s/2)
    current_idx = 0
    closest = min_subset_sum_diff_brute_force_recursive(arr, current_idx, find)
    return s - (2*closest)


def min_subset_sum_diff_brute_force_recursive(arr: list, current_idx: int, find: int) -> int:

    if current_idx >= len(arr):
        return 0

    if find == 0:
        return 0

    sum1 = 0
    if arr[current_idx] <= find:
        sum1 = arr[current_idx] + min_subset_sum_diff_brute_force_recursive(arr, current_idx+1, find-arr[current_idx])

    sum2 = min_subset_sum_diff_brute_force_recursive(arr, current_idx+1, find)

    max_sum = max(sum1, sum2)

    return max_sum


print("======================recursive brute force=========================")
print(min_subset_sum_diff([1, 2, 3, 9]))
print(min_subset_sum_diff([1, 2, 7, 1, 5]))
print(min_subset_sum_diff([1, 3, 100, 4]))


def min_subset_sum_diff_top_bottom(arr: list) -> int:
    s = sum(arr)
    find = 0
    if s%2 == 0:
        find = int(s/2)
    else:
        find = math.floor(s/2)
    current_idx = 0
    dp = [[-1 for i in range(find+1)] for j in range(len(arr))]
    closest = 0
    closest = min_subset_sum_diff_top_bottom_dp(arr, current_idx, find, dp)
    return s - (2*closest)


def min_subset_sum_diff_top_bottom_dp(arr: list, current_idx: int, find: int, dp: list) -> int:
    if find == 0:
        return 0
    if current_idx >= len(arr):
        return 0

    if dp[current_idx][find] != -1:
        return dp[current_idx][find]

    sum1 = 0
    if arr[current_idx] <= find:
        sum1 = arr[current_idx] + min_subset_sum_diff_top_bottom_dp(arr, current_idx+1, find-arr[current_idx], dp)

    sum2 = min_subset_sum_diff_top_bottom_dp(arr, current_idx+1, find, dp)

    dp[current_idx][find] = max(sum1, sum2)

    return dp[current_idx][find]


print("======================dp top bottom=========================")
print(min_subset_sum_diff_top_bottom([1, 2, 3, 9]))
print(min_subset_sum_diff_top_bottom([1, 2, 7, 1, 5]))
print(min_subset_sum_diff_top_bottom([1, 3, 100, 4]))



def can_partition(num):
  s = sum(num)
  dp = [[-1 for x in range(s+1)] for y in range(len(num))]
  return can_partition_recursive(dp, num, 0, 0, 0)


def can_partition_recursive(dp, num, currentIndex, sum1, sum2):
  # base check
  if currentIndex == len(num):
    return abs(sum1 - sum2)

  # check if we have not already processed similar problem
  if dp[currentIndex][sum1] == -1:
    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1 + num[currentIndex], sum2)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1, sum2 + num[currentIndex])

    dp[currentIndex][sum1] = min(diff1, diff2)

  return dp[currentIndex][sum1]



print("======================dp top bottom using two subset sum=========================")
print(can_partition([1, 2, 3, 9]))
print(can_partition([1, 2, 7, 1, 5]))
print(can_partition([1, 3, 100, 4]))


def min_subset_sum_diff_bottom_up(arr: list) -> int:

    n = len(arr)
    if n == 0:
        return -1

    array_sum = sum(arr)
    find = 0
    if array_sum%2 == 0:
        find = int(array_sum/2)
    else:
        find = math.floor(array_sum/2)
    dp = [[0 for i in range(find+1)] for j in range(len(arr))]

    for i in range(1, find+1):
        if arr[0] <= i:
            dp[0][i] = arr[0]

    for j in range(len(arr)):
        dp[j][0] = 0


    for i in range(1, len(arr)):
        for s in range(1, find+1):
            sum1, sum2 = 0, 0
            sum1 = dp[i-1][s]

            if arr[i] <= s:
                sum2 = arr[i] + dp[i-1][s-arr[i]]

            dp[i][s] = max(sum1, sum2)

    return array_sum - (2*dp[n-1][find])


print("======================dp bottom up tabular=========================")
print(min_subset_sum_diff_bottom_up([1, 2, 3, 9]))
print(min_subset_sum_diff_bottom_up([1, 2, 7, 1, 5]))
print(min_subset_sum_diff_bottom_up([1, 3, 100, 4]))

