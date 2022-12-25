"""
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

example1:
    Input: [1, 5, 12, 2, 11, 5], K = 3
    Output: 5
    Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

example2:
    Input: [1, 5, 12, 2, 11, 5], K = 4
    Output: 5
    Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

example3:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: 11
    Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

Similar problems:
    1. Find the Kth largest number in an unsorted array.
    2. Find the median of an unsorted array.
    3. Find the ‘K’ smallest or largest numbers in an unsorted array.
"""


import math
import heapq


def find_Kth_smallest_number_brute_force(nums, k):
    """
    Determine first smallest then second then third and so on until we find kth smallest.
    time complexity -> O(N*K)
    """
    previous_smallest_num = -math.inf
    current_smallest_num = math.inf
    current_smallest_index = -1
    previous_smallest_index = -1
    for i in range(k):
        for j in range(len(nums)):
            if nums[j] < current_smallest_num and nums[j] > previous_smallest_num:
                current_smallest_num = nums[j]
                current_smallest_index = j
            elif nums[j] == previous_smallest_num and j > previous_smallest_index:
                current_smallest_num = nums[j]
                current_smallest_index = j
                break

        previous_smallest_num = current_smallest_num
        previous_smallest_index = current_smallest_index
        current_smallest_num = math.inf

    return previous_smallest_num


print(
    "Kth smallest number using brute force is: "
    + str(find_Kth_smallest_number_brute_force([1, 5, 12, 2, 11, 5], 3))
)
print(
    "Kth smallest number using brute force is: "
    + str(find_Kth_smallest_number_brute_force([1, 5, 12, 2, 11, 5], 4))
)
print(
    "Kth smallest number using brute force is: "
    + str(find_Kth_smallest_number_brute_force([5, 12, 11, -1, 12], 3))
)


def find_Kth_smallest_number_sorting(nums, k):
    """
    sorting the nums first and then picking kth largest.
    Time complexity -> O(N logN)
    """
    return sorted(nums)[k - 1]


print(
    "Kth smallest number using sorting is: "
    + str(find_Kth_smallest_number_sorting([1, 5, 12, 2, 11, 5], 3))
)
print(
    "Kth smallest number using sorting is: "
    + str(find_Kth_smallest_number_sorting([1, 5, 12, 2, 11, 5], 4))
)
print(
    "Kth smallest number using sorting is: "
    + str(find_Kth_smallest_number_sorting([5, 12, 11, -1, 12], 3))
)


def find_Kth_smallest_number_max_heap(nums, k):
    """
    Finding kth smallest using max heap
    time complexity -> O(klogk) + O((N-k)logk)
    """

    max_heap = []
    n = len(nums)

    for i in range(k):
        heapq.heappush(max_heap, -nums[i])

    for i in range(k, n):
        if -nums[i] > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -nums[i])

    return -max_heap[0]


print(
    "Kth smallest number using max heap is: "
    + str(find_Kth_smallest_number_max_heap([1, 5, 12, 2, 11, 5], 3))
)
print(
    "Kth smallest number using max heap is: "
    + str(find_Kth_smallest_number_max_heap([1, 5, 12, 2, 11, 5], 4))
)
print(
    "Kth smallest number using max heap is: "
    + str(find_Kth_smallest_number_max_heap([5, 12, 11, -1, 12], 3))
)


def find_Kth_smallest_number_min_heap(nums, k):
    """
    Finding kth smallest number using min heap
    time complexity -> O(klogk) + O((N-k)logk)
    """

    min_heap = []
    n = len(nums)
    k = n - (k - 1)

    for i in range(k):
        heapq.heappush(min_heap, nums[i])

    for i in range(k, n):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])

    return min_heap[0]


print(
    "Kth smallest number using min heap is: "
    + str(find_Kth_smallest_number_min_heap([1, 5, 12, 2, 11, 5], 3))
)
print(
    "Kth smallest number using min heap is: "
    + str(find_Kth_smallest_number_min_heap([1, 5, 12, 2, 11, 5], 4))
)
print(
    "Kth smallest number using min heap is: "
    + str(find_Kth_smallest_number_min_heap([5, 12, 11, -1, 12], 3))
)


def find_Kth_smallest_number_partition_scheme_quick_sort(nums, k, start, high):
    """
    partition scheme quick sort.
    Quicksort picks a number called pivot and partition the input array around it.
    After partitioning, all numbers smaller than the pivot are to the left of the pivot,
    and all numbers greater than or equal to the pivot are to the right of the pivot.
    This ensures that the pivot has reached its correct sorted position.
    """

    p = partition(nums, start, high)
    if p == k - 1:
        return nums[p]

    if k - 1 > p:
        return find_Kth_smallest_number_partition_scheme_quick_sort(
            nums, k, p + 1, high
        )

    return find_Kth_smallest_number_partition_scheme_quick_sort(nums, k, 0, p - 1)


def partition(nums, low, high):
    if low == high:
        return low
    pivot = nums[high]
    start = low
    for i in range(low, high):
        if nums[i] < pivot:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1

    nums[start], nums[high] = nums[high], nums[start]

    return start


print(
    "Kth smallest number using quick sort partitioning is: "
    + str(
        find_Kth_smallest_number_partition_scheme_quick_sort(
            [1, 5, 12, 2, 11, 5], 3, 0, 5
        )
    )
)
print(
    "Kth smallest number using quick sort partitioning is: "
    + str(
        find_Kth_smallest_number_partition_scheme_quick_sort(
            [1, 5, 12, 2, 11, 5], 4, 0, 5
        )
    )
)
print(
    "Kth smallest number using quick sort partitioning is: "
    + str(
        find_Kth_smallest_number_partition_scheme_quick_sort(
            [5, 12, 11, -1, 12], 3, 0, 4
        )
    )
)


import random


def find_Kth_smallest_number_randomized_quick_select(nums, k, start, high):
    """
    Adding randomization for better performance in above implementation.
    Expected time complexity of the above algorithm will be O(N).
    but the absolute worst case is still O(N^2)
    Practically, this algorithm is a lot faster than the non-randomized version.
    """

    p = partition_randomized(nums, start, high)

    if p == k - 1:
        return nums[p]

    if k - 1 > p:
        return find_Kth_smallest_number_randomized_quick_select(nums, k, p + 1, high)

    return find_Kth_smallest_number_randomized_quick_select(nums, k, start, p - 1)


def partition_randomized(nums, start, high):
    if start == high:
        return start

    random_pivot = random.randint(start, high)
    nums[high], nums[random_pivot] = nums[random_pivot], nums[high]

    pivot = nums[high]
    low = start
    for i in range(start, high):
        if nums[i] < pivot:
            nums[i], nums[low] = nums[low], nums[i]
            low += 1
    nums[high], nums[low] = nums[low], nums[high]

    return low


print(
    "Kth smallest number using randomized quick select partitioning is: "
    + str(
        find_Kth_smallest_number_randomized_quick_select([1, 5, 12, 2, 11, 5], 3, 0, 5)
    )
)
print(
    "Kth smallest number using randomized quick select partitioning is: "
    + str(
        find_Kth_smallest_number_randomized_quick_select([1, 5, 12, 2, 11, 5], 4, 0, 5)
    )
)
print(
    "Kth smallest number using randomized quick select partitioning is: "
    + str(
        find_Kth_smallest_number_randomized_quick_select([5, 12, 11, -1, 12], 3, 0, 4)
    )
)


def find_Kth_smallest_number_using_median_of_medians(nums, k, start, high):
    """
    We can use the Median of Medians algorithm to choose a good pivot for the partitioning algorithm of the Quicksort.
    This algorithm finds an approximate median of an array in linear time O(N).
    When this approximate median is used as the pivot, the worst-case complexity of the partitioning procedure reduces to linear O(N).
    """

    p = partition_median_of_medians(nums, start, high)

    if p == k - 1:
        return nums[p]

    if k - 1 > p:
        return find_Kth_smallest_number_using_median_of_medians(nums, k, p + 1, high)

    return find_Kth_smallest_number_using_median_of_medians(nums, k, start, p - 1)


def partition_median_of_medians(nums, start, high):
    if start == high:
        return start

    median = find_median_of_medians(nums, start, high)

    for i in range(start, high):
        if nums[i] == median:
            nums[i], nums[high] = nums[high], nums[i]
            break

    pivot = nums[high]
    low = start
    for i in range(start, high):
        if nums[i] < pivot:
            nums[i], nums[low] = nums[low], nums[i]
            low += 1

    nums[low], nums[high] = nums[high], nums[low]

    return low


def find_median_of_medians(nums, low, high):
    n = high - low + 1
    # if we have less than 5 elements, ignore the partitioning algorithm
    if n < 5:
        return nums[low]

    # partition the given array into chunks of 5 elements
    partitions = [nums[j : j + 5] for j in range(low, high + 1, 5)]

    # for simplicity, lets ignore any partition with less than 5 elements
    fullPartitions = [partition for partition in partitions if len(partition) == 5]

    # sort all partitions
    sortedPartitions = [sorted(partition) for partition in fullPartitions]

    # find median of all partations; the median of each partition is at index '2'
    medians = [partition[2] for partition in sortedPartitions]

    return partition_median_of_medians(medians, 0, len(medians) - 1)


print(
    "Kth smallest number using median of medians is: "
    + str(
        find_Kth_smallest_number_using_median_of_medians([1, 5, 12, 2, 11, 5], 3, 0, 5)
    )
)
print(
    "Kth smallest number using median of medians is: "
    + str(
        find_Kth_smallest_number_using_median_of_medians([1, 5, 12, 2, 11, 5], 4, 0, 5)
    )
)
print(
    "Kth smallest number using median of medians is: "
    + str(
        find_Kth_smallest_number_using_median_of_medians([5, 12, 11, -1, 12], 3, 0, 4)
    )
)
