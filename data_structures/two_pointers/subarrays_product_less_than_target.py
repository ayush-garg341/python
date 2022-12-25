"""
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays
whose product is less than the target number.

example1:
    Input: [2, 5, 3, 10], target=30
    Output: [2], [5], [2, 5], [3], [5, 3], [10]
    Explanation: There are six contiguous subarrays whose product is less than the target.

example2:
    Input: [8, 2, 6, 5], target=50
    Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
    Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

from collections import deque


def find_subarrays(arr, target):
    results = []
    window_start = 0
    product = 1
    count = 0
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        product *= right_char

        while product >= target and window_start < len(arr):
            product = product / arr[window_start]
            window_start += 1

        if window_end - window_start >= 0:
            count += window_end - window_start + 1

        temp_list = deque()
        for i in range(window_end, window_start - 1, -1):
            temp_list.appendleft(arr[i])
            results.append(list(temp_list))

    print("count == ", count)

    return results


print(find_subarrays([2, 5, 3, 10], 30))
print(find_subarrays([8, 2, 6, 5], 50))
print(find_subarrays([5, 10, 2], 10))


def find_subarrays_simpler(arr, target):
    result = []
    # TODO: Write your code here
    window_start = 0
    for window_end in range(len(arr)):
        window_start = window_end
        product = 1
        temp_res = deque()
        while window_start >= 0:
            product *= arr[window_start]
            if product < target:
                temp_res.appendleft(arr[window_start])
                result.append(list(temp_res))
            else:
                break
            window_start -= 1

    return result


print("======= Using simpler approach ======== ")
print(find_subarrays_simpler([2, 5, 3, 10], 30))
print(find_subarrays_simpler([8, 2, 6, 5], 50))
print(find_subarrays_simpler([5, 10, 2], 10))


def num_subarrays_less_than_target(arr, target):
    """
    TC -> O(N)
    """
    window_start = 0
    count = 0
    product = 1
    for window_end in range(len(arr)):
        if arr[window_end] < target:
            count += 1
        product *= arr[window_end]
        while product >= target and window_start < window_end:
            product //= arr[window_start]
            window_start += 1
        count += window_end - window_start
    return count


print(" ===== Only count ====== ")
print(num_subarrays_less_than_target([10, 5, 2, 6], 100))
