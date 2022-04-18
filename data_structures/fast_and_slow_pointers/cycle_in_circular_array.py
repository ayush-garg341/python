"""
Write a method to determine if the array has a cycle. The cycle should have more than one element
and should follow one direction which means the cycle should not contain both forward and backward movements.

example1:
    Input: [1, 2, -1, 2, 2]
    Output: true
    Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

example2:
    Input: [2, 2, -1, 2]
    Output: true
    Explanation: The array has a cycle among indices: 1 -> 3 -> 1

example3:
    Input: [2, 1, -1, -2]
    Output: false
    Explanation: The array does not have any cycle.
"""


def circular_array_loop_exist(arr):
    for i in arr:
        is_forward = arr[i] >= 0
        slow, fast = i, i

        while True:
            slow = get_next_index(arr, slow, is_forward)
            fast = get_next_index(arr, fast, is_forward)

            if fast != -1:
                fast = get_next_index(arr, fast, is_forward)
            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True

    return False


def get_next_index(arr, current_index, is_forward):
    direction = arr[current_index] >= 0

    if direction != is_forward:
        return -1

    next_idx = (current_index + arr[current_index]) % len(arr)
    if next_idx == current_index:
        next_idx = -1

    return next_idx


print(circular_array_loop_exist([1, 2, -1, 2, 2]))
print(circular_array_loop_exist([2, 2, -1, 2]))
print(circular_array_loop_exist([2, 1, -1, -2]))
