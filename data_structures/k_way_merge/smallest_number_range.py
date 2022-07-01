"""
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

example1:
    Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
    Output: [4, 7]
    Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

example2:
    Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
    Output: [9, 12]
    Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
"""

import heapq
import math


def find_smallest_range(lists):
    """
    Time complexity -> O(Nlog(M))
    N - total number of elements in all M lists.
    M - total number of lists
    """
    current_max_number = -math.inf
    min_heap = []
    min_range = math.inf
    num1, num2 = None, None
    for i in range(len(lists)):
        current_max_number = max(current_max_number, lists[i][0])
        heapq.heappush(min_heap, (lists[i][0], i, 0))

    while len(min_heap) == len(lists):
        (min_elt, list_index, elt_index) = heapq.heappop(min_heap)
        diff = abs(current_max_number - min_elt)
        if diff < min_range:
            min_range = diff
            num1 = min_elt
            num2 = current_max_number
        if elt_index < len(lists[list_index]) - 1:
            current_max_number = max(current_max_number, lists[list_index][elt_index + 1])
            heapq.heappush(min_heap, (lists[list_index][elt_index + 1], list_index, elt_index + 1))
        else:
            break

    return [num1, num2]


def main():
    print("Smallest range is: " + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
    print("Smallest range is: " + str(find_smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])))
    print("Smallest range is: " + str(find_smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]])))


main()
