"""
Write a function that taken in an array of atleast two integers and that returns an array of the starting and ending indices of the smallest
subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted.

ex:
    input -> [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    output -> [3, 9]

optimal complexity
    Time -> O(N)
    Space -> O(1)
"""


def subarray_sort(array):
    """
    Time complexity -> O(N logN)
    space complexity -> O(N)
    """
    sorted_arr = sorted(array)
    result = [-1, -1]
    for i in range(len(array)):
        if array[i] != sorted_arr[i]:
            if result[0] == -1:
                result[0] = i
            else:
                result[1] = i

    return result


print(subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))

print("Optimized vversionn")


def subarraySortOptmizie(array):
    n = len(array)
    # find start index of unsorted array
    start_idx = -1
    max_so_far = array[0]
    for i in range(1, n):
        if array[i] < array[i - 1]:
            start_idx = i
            max_so_far = array[i]
            break

    if start_idx == -1:
        return [-1, -1]

    # find end index of unsorted array
    end_idx = -1
    for i in range(n - 2, -1, -1):
        if array[i] > array[i + 1] or array[i] < max_so_far:
            end_idx = i
            break

    # find the min and max element in the range start_idx to end_idx
    min_elt = array[start_idx]
    max_elt = array[end_idx]
    for i in range(start_idx, end_idx + 1):
        if array[i] < min_elt:
            min_elt = array[i]
        elif array[i] > max_elt:
            max_elt = array[i]

    # check the correct position of min element
    start_pos = -1
    for i in range(n):
        if array[i] > min_elt:
            start_pos = i
            break
    # check the correct position of max element
    end_pos = -1
    for i in range(n - 1, -1, -1):
        if array[i] < max_elt:
            end_pos = i
            break

    return [start_pos, end_pos]


print(subarraySortOptmizie([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
print(subarraySortOptmizie([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))
print(subarraySortOptmizie([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))
