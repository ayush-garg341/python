"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

example1:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' apeared twice.

example2:
    Input: [5, 12, 11, 3, 11], K = 2
    Output: [11, 5] or [11, 12] or [11, 3]
    Explanation: Only '11' appeared twice, all other numbers appeared once.
"""

import heapq


def find_k_frequent_numbers(nums, k):
    topNumbers = []
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1

    if k >= len(freq):
        return freq.keys()

    min_heap = []
    for key, val in freq.items():
        heapq.heappush(min_heap, (val, key))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    while len(min_heap):
        topNumbers.append(heapq.heappop(min_heap)[1])

    return topNumbers


def main():

    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
