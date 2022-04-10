"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

example1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.

example2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
"""


def find_triplets_adding_to_zero(nums: list) -> list:
    triplets_arr = []

    nums.sort()
    for num in nums:
        a, b = pair_with_target_sum(nums, -num)
        if a is not None and b is not None:
            triplets_arr.append([num, a, b])

    return triplets_arr


def pair_with_target_sum(arr, target_sum):
    start = 0
    end = len(arr) - 1

    while start < end:
        s = arr[start] + arr[end]
        if s == target_sum:
            return (arr[start], arr[end])

        elif s > target_sum:
            end -= 1

        else:
            start += 1

    return (None, None)


print(find_triplets_adding_to_zero([-3, 0, 1, 2, -1, 1, -2]))
print(find_triplets_adding_to_zero([-5, 2, -1, -2, 3]))
