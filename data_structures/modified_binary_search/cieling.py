"""
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

example1:
    Input: [4, 6, 10], key = 6
    Output: 1
    Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

example2:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: 4
    Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

example3:
    Input: [4, 6, 10], key = 17
    Output: -1
    Explanation: There is no number greater than or equal to '17' in the given array.
"""


def search_ceiling_of_a_number(arr, key):
    # TODO: Write your code here
    if len(arr) == 0 or arr[len(arr) - 1] < key:
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
    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
