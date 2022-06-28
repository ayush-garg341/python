"""
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
"""

import heapq


def find_Kth_smallest(lists, k):
    """
    Time complexity : O(N*log(k))
    N - total number of elements in all the lists
    k - kth smallest
    """
    min_heap = []
    for each_list in lists:
        for num in each_list:
            if len(min_heap) < k:
                heapq.heappush(min_heap, -num)
            else:
                if -num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, -num)
    return -min_heap[0]


def find_Kth_smallest_optmized_way(lists, k):
    """
    Time complexity - O(k*log(M))
    k - kth smallest
    M - Number of lists
    We need not to put k elements in heap.
    We can use merge array approach and keep only M elements one from each list.
    When we found kth element that will be smallest and we can stop processing further.
    """
    min_heap = []
    for i in range(len(lists)):
        heapq.heappush(min_heap, (lists[i][0], i, 0))

    count = 0

    while len(min_heap):
        (elt, list_index, elt_index) = heapq.heappop(min_heap)
        count += 1
        if count == k:
            return elt
        if elt_index < len(lists[list_index]) - 1:
            heapq.heappush(min_heap, (lists[list_index][elt_index + 1], list_index, elt_index + 1))


"""
Problem - Given ‘M’ sorted arrays, find the median number among all arrays.
Solution - This problem is similar to our parent problem with K=Median.
So if there are ‘N’ total numbers in all the arrays we need to find the K’th minimum number where K=N/2

"""


def main():
    # print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    # print("Kth smallest number is: " + str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))
    # print("Kth smallest number is: " + str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))
    # print("Kth smallest number is: " + str(find_Kth_smallest([[1, 2], [1, 3]], 1)))
    print(" ----------------------- ")
    # print("Kth smallest number is: " + str(find_Kth_smallest_optmized_way([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    # print("Kth smallest number is: " + str(find_Kth_smallest_optmized_way([[5, 8, 9], [1, 7]], 3)))
    print("Kth smallest number is: " + str(find_Kth_smallest_optmized_way([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))
    # print("Kth smallest number is: " + str(find_Kth_smallest_optmized_way([[1, 2], [1, 3]], 1)))


main()
