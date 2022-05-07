"""
Runs in O(n) expected time.
Also known as prune-and-search or decrease-and-conquer.
"""

import random


def randomized_quick_select(nums, k):
    if len(nums) == 1:
        return nums[0]
    pivot = random.choice(nums)

    L = [x for x in nums if x < pivot]
    E = [x for x in nums if x == pivot]
    G = [x for x in nums if x > pivot]

    if k <= len(L):
        return randomized_quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot
    else:
        j = k - len(L) - len(E)
        return randomized_quick_select(G, j)


nums = [1, 5, 3, 2, 9, 7, 8]
print(randomized_quick_select(nums, 4))
print(randomized_quick_select(nums, 7))
