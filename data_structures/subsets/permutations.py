"""
Given a set of distinct numbers, find all of its permutations.
Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following
six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}

If a set has ‘n’ distinct elements it will have n! permutations.
"""

from collections import deque


def find_permutations(nums):
    result = []
    if len(nums) == 0:
        return result
    permutations = deque()
    permutations.append([])
    for current_num in nums:
        n = len(permutations)
        for _ in range(n):
            left = permutations.popleft()
            for i in range(len(left) + 1):
                new_per = list(left)
                new_per.insert(i, current_num)
                if len(new_per) == len(nums):
                    result.append(new_per)
                else:
                    permutations.append(new_per)
    return result


def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result


def generate_permutations_recursive(nums, index, current_per, result):
    if index == len(nums):
        result.append(current_per)
    else:
        for i in range(len(current_per) + 1):
            new_per = list(current_per)
            new_per.insert(i, nums[index])
            generate_permutations_recursive(nums, index + 1, new_per, result)


def swap_char(nums, i, j):
    new_nums = nums.copy()
    new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
    return new_nums


def permute_rec(nums, current_idx, result):
    if current_idx == len(nums) - 1:
        result.append(nums)
        return

    for i in range(current_idx, len(nums)):
        swapped = swap_char(nums, current_idx, i)
        permute_rec(swapped, current_idx + 1, result)


def generate_permutations_loop(nums):
    result = []
    permute_rec(nums, 0, result)
    return result


def main():
    print("Here are all the permutations ==  " + str(find_permutations([1, 3, 5])))
    print("Here are all the permutations == " + str(generate_permutations([1, 3, 5])))
    print(
        "Here are all the permutations == " + str(generate_permutations_loop([1, 3, 5]))
    )


main()
