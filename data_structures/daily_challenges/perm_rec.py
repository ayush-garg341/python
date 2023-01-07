"""
Given a set of distinct numbers, find all of its permutations.
"""


def find_perm(nums):
    result = []
    find_perm_rec(nums, result, [], 0)
    return result


def find_perm_rec(nums, result, current_perm, idx):
    if idx == len(nums):
        result.append(current_perm)
    else:
        for pos in range(len(current_perm) + 1):
            new = current_perm.copy()
            new.insert(pos, nums[idx])
            find_perm_rec(nums, result, new, idx + 1)


print(find_perm([1, 2, 3]))
