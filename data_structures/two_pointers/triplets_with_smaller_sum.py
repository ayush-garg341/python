"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.

example1:
    Input: [-1, 0, 2, 3], target=3
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

example2:
    Input: [-1, 4, 2, 1, 3], target=5
    Output: 4
    Explanation: There are four triplets whose sum is less than the target:
       [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""


def triplet_with_smaller_sum(arr, target):
    count = 0

    arr.sort()

    for i in range(len(arr)):
        target_sum = target - arr[i]
        start = i + 1
        end = len(arr) - 1

        while start < end:
            actual_sum = arr[start] + arr[end]
            if actual_sum < target_sum:
                count += end - start
                start += 1
            else:
                end -= 1

    return count


print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


def find_triplets_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        target_sum = target - arr[i]
        start = i + 1
        end = len(arr) - 1

        while start < end:
            actual_sum = arr[start] + arr[end]
            if actual_sum < target_sum:
                for j in range(end, start, -1):
                    triplets.append([arr[i], arr[start], arr[j]])
                start += 1
            else:
                end -= 1

    return triplets


print(find_triplets_with_smaller_sum([-1, 0, 2, 3], 3))
print(find_triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))
