"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
"""


def max_sum_size_k_brute_force(arr: list, k: int) -> int:
    max_sum = 0
    for i in range(0, len(arr) - k + 1):
        sum_k = 0
        for window in range(i, i + k):
            sum_k += arr[window]
            max_sum = max(max_sum, sum_k)
    return max_sum


print(max_sum_size_k_brute_force([2, 1, 5, 1, 3, 2], 3))
print(max_sum_size_k_brute_force([2, 3, 4, 1, 5], 2))


def max_sum_sub_array_size_k(arr: list, k: int) -> int:
    max_sum = 0
    window_start = 0
    sum_k = 0
    for window_end in range(0, len(arr)):
        sum_k += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, sum_k)
            sum_k -= arr[window_start]
            window_start += 1

    return max_sum


print(max_sum_sub_array_size_k([2, 1, 5, 1, 3, 2], 3))
print(max_sum_sub_array_size_k([2, 3, 4, 1, 5], 2))
