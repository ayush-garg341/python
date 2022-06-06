"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the,
array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

example1:
    Input: [4, 6, 10], key = 10
    Output: 2
example2:
    Input: [1, 2, 3, 4, 5, 6, 7], key = 5
    Output: 4
example3:
    Input: [10, 6, 4], key = 10
    Output: 0
"""


def binary_search(arr, key):
    # TODO: Write your code here
    index = -1
    if len(arr) == 0:
        return index
    ascending = False
    size = len(arr)
    if arr[0] <= arr[size - 1]:
        ascending = True

    start = 0
    end = size - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid

        if ascending:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return index


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
