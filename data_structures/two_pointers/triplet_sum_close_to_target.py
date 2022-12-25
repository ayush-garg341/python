"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to
the target number as possible, return the sum of the triplet.

example1:
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

example2:
    Input: [-3, -1, 1, 2], target=1
    Output: 0
    Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

example3:
    Input: [1, 0, 1, 1], target=100
    Output: 3
    Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""

import math


def triplet_sum_closest_to_target(arr, target_sum):
    arr.sort()
    closest_sum = math.inf
    triplet_arr = [0, 0, 0]
    s = math.inf

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        target = target_sum - arr[i]
        start = i + 1
        end = len(arr) - 1
        while start < end:
            actual_sum = arr[start] + arr[end]
            if actual_sum == target:
                triplet_arr[0], triplet_arr[1], triplet_arr[2] = (
                    arr[i],
                    arr[start],
                    arr[end],
                )
                return target_sum
            elif actual_sum > target:
                abs_val = abs(target - actual_sum)
                if closest_sum > abs_val:
                    closest_sum = abs_val
                    triplet_arr[0], triplet_arr[1], triplet_arr[2] = (
                        arr[i],
                        arr[start],
                        arr[end],
                    )
                    s = arr[i] + arr[start] + arr[end]
                end -= 1
            else:
                abs_val = abs(target - actual_sum)
                if closest_sum > abs_val:
                    closest_sum = abs_val
                    triplet_arr[0], triplet_arr[1], triplet_arr[2] = (
                        arr[i],
                        arr[start],
                        arr[end],
                    )
                    s = arr[i] + arr[start] + arr[end]
                start += 1

    print("triplet is ---- ", triplet_arr[0], triplet_arr[1], triplet_arr[2])
    return s


print(triplet_sum_closest_to_target([-2, 0, 1, 2], 2))
print(triplet_sum_closest_to_target([-3, -1, 1, 2], 1))
print(triplet_sum_closest_to_target([1, 0, 1, 1], 100))
