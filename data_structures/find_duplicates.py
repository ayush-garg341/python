"""
Find elements in an array which occurs more than once in O(n). And using
constant extra space.
In an array of N elements we have elements 0 -> N-1
"""

arr = [6, 2, 3, 3, 2, 4, 5, 6, 4]

def find_dup(arr):
    size = len(arr)
    for i in range(0, len(arr)):
        idx = arr[i] % size
        arr[idx] = arr[idx] + size

    for i in range(0, len(arr)):
        if arr[i] >= 2*size:
            print("repeating element = ", i)
            # can also detect number of times an element is repeating with modulo size.


find_dup(arr)
