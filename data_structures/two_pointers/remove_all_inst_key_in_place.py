"""
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and
return the new length of the array.

example1:
    Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
    Output: 4
    Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

example2:
    Input: [2, 11, 2, 2, 1], Key=2
    Output: 2
    Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""


def remove_all_instance_key_inplace(arr, key):
    start = 0
    for i in range(len(arr)):
        if arr[i] == key:
            continue
        else:
            arr[start] = arr[i]
            start += 1

    return arr[0:start]


print(remove_all_instance_key_inplace([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_all_instance_key_inplace([2, 11, 2, 2, 1], 2))
