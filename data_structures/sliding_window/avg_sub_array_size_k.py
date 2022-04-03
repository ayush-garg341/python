"""
Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
"""


def avg_sub_array(arr: list, k: int) -> list:
    start = 0
    end = len(arr)
    sum_k = 0
    result = []
    window_start = 0
    for window_end in range(start, end):
        sum_k += arr[window_end]

        if window_end >= k - 1:
            result.append(sum_k / k)
            sum_k -= arr[window_start]
            window_start += 1

    return result


print(avg_sub_array([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
