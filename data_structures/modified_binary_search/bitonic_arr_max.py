"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically
increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i
in the array arr[i] != arr[i+1].

example1:
    Input: [1, 3, 8, 12, 4, 2]
    Output: 12
    Explanation: The maximum number in the input bitonic array is '12'.

example2:
    Input: [3, 8, 3, 1]
    Output: 8

exmaple3:
    Input: [1, 3, 8, 12]
    Output: 12

example4:
    Input: [10, 9, 8]
    Output: 10
"""


def find_max_in_bitonic_array(arr):
    # TODO: Write your code here
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
