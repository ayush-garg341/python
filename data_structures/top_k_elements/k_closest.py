"""
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

example1:
    Input: [5, 6, 7, 8, 9], K = 3, X = 7
    Output: [6, 7, 8]

example2:
    Input: [2, 4, 5, 6, 9], K = 3, X = 6
    Output: [4, 5, 6]

example3:
    Input: [2, 4, 5, 6, 9], K = 3, X = 10
    Output: [5, 6, 9]
"""

import heapq


def find_closest_elements(arr, K, X):
    result = [None] * K
    max_heap = []
    for i in range(K):
        heapq.heappush(max_heap, (-abs(X - arr[i]), arr[i]))
    for i in range(K, len(arr)):
        if -abs(X - arr[i]) > max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-abs(X - arr[i]), arr[i]))
    i = K - 1
    while len(max_heap):
        max_elt = heapq.heappop(max_heap)
        result[i] = max_elt[1]
        i -= 1

    result.sort()

    return result


from collections import deque


def find_closest_elements_two_pointers(arr, k, x):
    index = binary_search(arr, x)
    if index == len(arr):
        return arr[len(arr) - k :]

    if index == 0:
        return arr[:k]
    high = index
    low = index - 1

    # keeping index - 1 on low side since giving priority to lower elements in ascending order.
    # high = index + 1
    # low = index

    result = deque()
    while len(result) != k:
        if low < 0:
            result.append(arr[high])
            high += 1
        elif high > len(arr) - 1:
            result.appendleft(arr[low])
            low -= 1
        elif abs(x - arr[low]) <= abs(x - arr[high]):
            result.appendleft(arr[low])
            low -= 1
        else:
            result.append(arr[high])
            high += 1
    return result


def binary_search(nums, x):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif x < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low


def main():
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
    )

    print(" ======================= ")

    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements_two_pointers([5, 6, 7, 8, 9], 3, 7))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements_two_pointers([2, 4, 5, 6, 9], 3, 6))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements_two_pointers([2, 4, 5, 6, 9], 3, 10))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements_two_pointers([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
    )


main()
