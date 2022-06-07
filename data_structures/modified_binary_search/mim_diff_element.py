"""
Given an array of numbers sorted in ascending order, find the element in the array that has the
minimum difference with the given ‘key’.

Example1:
    Input: [4, 6, 10], key = 7
    Output: 6
    Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

Example2:
    Input: [4, 6, 10], key = 4
    Output: 4
"""


def search_min_diff_element(arr, key):
    # TODO: Write your code here
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return arr[mid]
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if start == 0:
        return arr[start]
    elif start == len(arr):
        return arr[start - 1]
    else:
        num1 = arr[start - 1]
        num2 = arr[start]
        if abs(num1 - key) < abs(num2 - key):
            return num1
        return num2


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
