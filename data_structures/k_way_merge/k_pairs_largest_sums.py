"""
Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum,
where each pair consists of numbers from both the arrays.

example1:
    Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
    Output: [9, 3], [9, 6], [8, 6]
    Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

example2:
    Input: L1=[5, 2, 1], L2=[2, -1], K=3
    Output: [5, 2], [5, -1], [2, 2]

Optmizations:
    1. Rather than going through all the elements in both the arrays, we can process k elements from both the arrays.
        That will give us max sum.
    2. As soon as we encounter sum of elements < top_element break it.
"""

import heapq


def find_k_largest_pairs(nums1, nums2, k):
    """
    Since, at most, we’ll be going through all the elements of both arrays and we will add/remove one element in
    the heap in each step, the time complexity of the above algorithm will be O(N*M*logK).
    If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to O(K^2logK),
    because we are not iterating more than ‘K’ elements in both arrays.
    """
    result = []
    min_heap = []

    for i_num in range(min(k, len(nums1))):
        for j_num in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heapq.heappush(min_heap, (nums1[i_num] + nums2[j_num], i_num, j_num))
            else:
                top_sum = min_heap[0][0]
                new_sum = nums1[i_num] + nums2[j_num]
                if new_sum > top_sum:
                    heapq.heappop(min_heap)
                    heapq.heappush(
                        min_heap, (nums1[i_num] + nums2[j_num], i_num, j_num)
                    )
                else:
                    break

    while len(min_heap):
        top_sum, i_num, j_num = heapq.heappop(min_heap)
        result.append((nums1[i_num], nums2[j_num]))

    return result


def find_Kth_smallest_pairs(nums1, nums2, k):
    result = []
    min_heap = []
    for i_num in range(min(k, len(nums1))):
        for j_num in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heapq.heappush(min_heap, (-(nums1[i_num] + nums2[j_num]), i_num, j_num))
            else:
                top_sum = min_heap[0][0]
                new_sum = nums1[i_num] + nums2[j_num]
                if -new_sum > top_sum:
                    heapq.heappop(min_heap)
                    heapq.heappush(
                        min_heap, (-(nums1[i_num] + nums2[j_num]), i_num, j_num)
                    )
                else:
                    break

    while len(min_heap):
        top_sum, i_num, j_num = heapq.heappop(min_heap)
        result.append((nums1[i_num], nums2[j_num]))

    return result


def main():
    print(
        "Pairs with largest sum are: "
        + str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))
    )
    print(
        "Pairs with largest sum are: "
        + str(find_k_largest_pairs([5, 2, 1], [2, -1], 3))
    )
    print(" ------------------------------------- ")
    print(
        "Paris with smallest sum are: "
        + str(find_Kth_smallest_pairs([1, 7, 11], [2, 4, 6], 3))
    )
    print(
        "Paris with smallest sum are: "
        + str(find_Kth_smallest_pairs([1, 1, 2], [1, 2, 3], 2))
    )


main()
