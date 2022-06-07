"""
Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the,
array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface
ArrayReader to read elements of the array.
ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index,
it will return Integer.MAX_VALUE

Example 1:
    Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
    Output: 6
    Explanation: The key is present at index '6' in the array.

Example2:
    Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
    Output: -1
    Explanation: The key is not present in the array.

The issue is we don't know the proper bounds for the array, we will first find out the proper bounds.
We will start from beginning and exponentially increase the size of bounds.
"""

import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # TODO: Write your code here
    start = 0
    end = 1
    bound_size = 2
    while key > reader.get(end):
        start = end + 1
        bound_size *= 2
        end = start + bound_size - 1
    return binary_search(reader, start, end, key)


def binary_search(reader, start, end, key):
    while start <= end:
        mid = (start + end) // 2
        if key == reader.get(mid):
            return mid
        elif key < reader.get(mid):
            end = mid - 1
        else:
            start = mid + 1
    return -1


def simple_search_in_infinite_array(reader, key):
    hi = 1
    while reader.get(hi) < key:
        hi *= 2

    low = hi // 2
    while low <= hi:
        mid = (low + hi) // 2
        val = reader.get(mid)
        if val == key:
            return mid
        elif key < val:
            hi = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(simple_search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    print(simple_search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(simple_search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))
    print(simple_search_in_infinite_array(reader, 200))


main()
