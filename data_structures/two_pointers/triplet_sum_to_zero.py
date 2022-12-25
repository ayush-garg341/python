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
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        num = nums[i]
        pair_with_target_sum(nums[i + 1 :], -num, triplets_arr)

    return triplets_arr


def pair_with_target_sum(arr, target_sum, triplets_arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        s = arr[start] + arr[end]
        if s == target_sum:
            triplets_arr.append([-target_sum, arr[start], arr[end]])
            start += 1
            end -= 1
            while start < end and arr[start] == arr[start - 1]:
                start += 1
            while start < end and arr[end] == arr[end + 1]:
                end -= 1

        elif s > target_sum:
            end -= 1

        else:
            start += 1


print(find_triplets_adding_to_zero([-3, 0, 1, 2, -1, 1, -2]))
print(find_triplets_adding_to_zero([-5, 2, -1, -2, 3]))


def find_triplets_adding_to_zero_another_approach(arr):
    triplets = []
    # TODO: Write your code here
    arr.sort()
    for i in range(len(arr)):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        start = i + 1
        end = len(arr) - 1
        target_sum = -(arr[i])
        while start < end:
            a = arr[start]
            b = arr[end]
            if a + b > target_sum:
                end -= 1
            elif a + b < target_sum:
                start += 1
            else:
                triplets.append([arr[i], arr[start], arr[end]])
                while start < len(arr) - 1:
                    if arr[start + 1] != arr[start]:
                        break
                    start += 1
                while end > 0:
                    if arr[end] != arr[end - 1]:
                        break
                    end -= 1
                start += 1
                end -= 1
    return triplets


print(find_triplets_adding_to_zero_another_approach([-3, 0, 1, 2, -1, 1, -2]))
print(find_triplets_adding_to_zero_another_approach([-5, 2, -1, -2, 3]))
