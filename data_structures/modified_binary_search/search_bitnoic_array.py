"""
Given a Bitonic array, find if a given ‘key’ is present in it.
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

example1:
    Input: [1, 3, 8, 4, 3], key=4
    Output: 3

example2:
    Input: [3, 8, 3, 1], key=8
    Output: 1

example3:
    Input: [1, 3, 8, 12], key=12
    Output: 3

example4:
    Input: [10, 9, 8], key=10
    Output: 0
"""


def search_bitonic_array(arr, key):
    # finding the peak element first.
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < arr[mid + 1]:
            start = mid + 1
        elif arr[mid] > arr[mid + 1]:
            end = mid
    if arr[start] == key:
        return start
    left_part = arr[0:start]
    right_part = arr[start + 1 :]

    index = binary_search(left_part, key)
    if index == -1:
        index = binary_search(right_part, key)
        if index != -1:
            index += start + 1

    return index


def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
