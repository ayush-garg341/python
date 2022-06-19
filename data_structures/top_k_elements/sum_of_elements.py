"""
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

example1:
    Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
    Output: 23
    Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
    between 5 and 15 is 23 (11+12).

example2:
    Input: [3, 5, 8, 7], and K1=1, K2=4
    Output: 12
    Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
    number (8) is 12 (5+7).
"""

import heapq


def find_sum_of_elements(nums, k1, k2):
    s = 0
    min_heap = []
    for i in range(len(nums)):
        heapq.heappush(min_heap, nums[i])

    k = 0
    while len(min_heap):
        if k >= k1 and k < k2 - 1:
            s += heapq.heappop(min_heap)
        elif k == k2 - 1:
            break
        else:
            heapq.heappop(min_heap)
        k += 1
    return s


def find_sum_of_elements_max_heap(nums, k1, k2):
    s = 0
    max_heap = []
    for i in range(len(nums)):
        if i < k2 - 1:
            heapq.heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -nums[i])

    for _ in range(k2 - k1 - 1):
        s += -heapq.heappop(max_heap)
    return s


def main():

    print(
        "Sum of all numbers between k1 and k2 smallest numbers: "
        + str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))
    )
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))

    print(" ============================ ")

    print(
        "Sum of all numbers between k1 and k2 smallest numbers: "
        + str(find_sum_of_elements_max_heap([1, 3, 12, 5, 15, 11], 3, 6))
    )
    print(
        "Sum of all numbers between k1 and k2 smallest numbers: "
        + str(find_sum_of_elements_max_heap([3, 5, 8, 7], 1, 4))
    )


main()
