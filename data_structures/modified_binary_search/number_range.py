"""
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

example1:
    Input: [4, 6, 6, 6, 9], key = 6
    Output: [1, 3]
example2:
    Input: [1, 3, 8, 10, 15], key = 10
    Output: [3, 3]
example3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: [-1, -1]
"""


def find_range(arr, key):
    result = [-1, -1]
    if len(arr) == 0:
        return result
    n = len(arr)
    start = 0
    end = n - 1
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            index = mid
            break
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if index == -1:
        return result
    begin = index
    while begin > 0:
        if arr[begin - 1] == key:
            begin -= 1
        else:
            break
    result[0] = begin

    end = index
    while end < n - 1:
        if arr[end + 1] == key:
            end += 1
        else:
            break
    result[1] = end
    return result


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
