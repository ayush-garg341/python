"""
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
You can assume that the array does not have any duplicates.

example1:
    Input: [10, 15, 1, 3, 8]
    Output: 2
    Explanation: The array has been rotated 2 times.

example2:
    Input: [4, 5, 7, 9, 10, -1, 2]
    Output: 5
    Explanation: The array has been rotated 5 times.

example3:
    Input: [1, 3, 8, 10]
    Output: 0
    Explanation: The array has been not been rotated.
"""


def count_rotations(arr):
    # TODO: Write your code here
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid + 1
        elif arr[mid] < arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    if start == len(arr) - 1:
        return 0
    return start + 1


def count_rotations_with_duplicates(arr):
    # TODO: Write your code here
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return mid
        elif arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1
        elif arr[mid] < arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    print("start == ", start)
    if start == len(arr) - 1:
        return 0
    return start % len(arr)


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
    # print(count_rotations_with_duplicates([1, 3, 5]))
    # print(count_rotations_with_duplicates([2, 2, 2, 0, 1]))
    print(count_rotations_with_duplicates([3, 1]))


main()
