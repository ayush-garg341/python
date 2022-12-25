"""
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index.
Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

1. If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
2. If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

Write a method to determine if the array has a cycle.
"""


def circular_array_loop_exists(arr):
    """
    TC - O(N^2)
    """
    if len(arr) == 1:
        return False
    for i in range(len(arr)):
        is_fwd = arr[i] >= 0
        slow = fast = i
        while True:
            slow = next_elt_circular_arr(slow, arr, is_fwd)
            fast = next_elt_circular_arr(fast, arr, is_fwd)
            if fast != -1:
                fast = next_elt_circular_arr(fast, arr, is_fwd)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False


def next_elt_circular_arr(idx, arr, direction):
    is_fwd = arr[idx] >= 0
    if is_fwd != direction:
        next_idx = -1
        return next_idx
    jump = arr[idx]
    next_idx = (idx + jump) % len(arr)
    if next_idx == idx:
        next_idx = -1
    return next_idx


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
