"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

example1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

example2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


def pair_with_target_sum(arr, target_sum):
    start = 0
    end = len(arr) - 1

    while start < end:
        s = arr[start] + arr[end]
        if s == target_sum:
            return [arr[start], arr[end]]

        elif s > target_sum:
            end -= 1

        else:
            start += 1

    return [-1, -1]


# print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
# print(pair_with_target_sum([2, 5, 9, 11], 11))
# print(pair_with_target_sum([2, 4, 6, 8], 11))

"""
Alternate approach
Iterate over all numbers and find the other number in remaining array using binary search.
TC -> O(NlogN)
"""


def pair_with_target_sum_binary_search(arr, target_sum):
    for i in range(len(arr)):
        other_num = target_sum - arr[i]
        binary_search_index = binary_search(arr[i + 1 :], other_num)
        if binary_search_index != -1:
            return [i, binary_search_index + i + 1]
    return [-1, -1]


def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(pair_with_target_sum_binary_search([1, 2, 3, 4, 6], 6))
print(pair_with_target_sum_binary_search([2, 5, 9, 11], 11))
print(pair_with_target_sum_binary_search([2, 4, 6, 8], 11))

"""
Alternate approach
Instead of using a two-pointer or a binary search approach, we can utilize a HashTable to search for the required pair.
"""


def pair_with_target_sum_hash_table(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [num, target_sum - num]
        else:
            nums[num] = 1

    return [-1, -1]


# print(pair_with_target_sum_hash_table([1, 2, 3, 4, 6], 6))
# print(pair_with_target_sum_hash_table([2, 5, 9, 11], 11))
# print(pair_with_target_sum_hash_table([2, 4, 6, 8], 11))
