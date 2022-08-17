"""
Find the largest range of numbers given an input array.
Range is defined as the numbers which comes right after each other on real line like 1, 2, 3, 4 ..

example1:
    input -> [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    output -> [0, 7]

example:
    input -> [1, 1, 1, 3, 4]
    output -> [3, 4]
"""

def largest_range_sort(arr):
    """
    TC -> O(NlogN)
    """
    arr.sort()

    largest_range = [arr[0], arr[0]]

    start = 0
    end = 0

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1 or arr[i] == arr[i-1]:
            end = i
            if arr[end] - arr[start] > largest_range[1] - largest_range[0]:
                largest_range[0] = arr[start]
                largest_range[1] = arr[end]
        else:
            start = i

    return largest_range


print(largest_range_sort([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
print(largest_range_sort([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))
print(largest_range_sort([1, 1, 1, 3, 4]))
