"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
sorting approach -> O(N Log N)
heap approach -> O(k log k + (N-k)log K)

example1:
    Input: [3, 1, 5, 12, 2, 11], K = 3
    Output: [5, 12, 11]

example2:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: [12, 11, 12]
"""

import heapq


def find_k_largest_numbers(nums, k):
    result = []
    min_heap = []
    for i in range(k):
        result.append(None)
        heapq.heappush(min_heap, nums[i])

    n = len(nums)
    for i in range(k, n):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])

    count = k - 1
    while len(min_heap):
        min_elt = heapq.heappop(min_heap)
        result[count] = min_elt
        count -= 1

    return result


def main():

    print(
        "Here are the top K numbers: "
        + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
    )

    print(
        "Here are the top K numbers: "
        + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3))
    )


main()
