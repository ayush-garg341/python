"""
Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’.
The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’.

Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.

ex1:
    Input: [4, 6, 10], key = 6
    Output: 1
    Explanation: The biggest number smaller than or equal to '6' is '6' having index '1'.
ex2:
    Input: [4, 6, 10], key = -1
    Output: -1
    Explanation: There is no number smaller than or equal to '-1' in the given array.
"""


def search_floor_of_a_number(arr, key):
    # TODO: Write your code here
    if len(arr) == 0 or key < arr[0]:
        return -1
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
    return end


def main():
    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))


main()
