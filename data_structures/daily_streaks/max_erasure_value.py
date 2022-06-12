"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.
An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is,
if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

example1:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].

example2:
    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
"""

from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    window_start = 0
    max_sum = 0
    current_sum = 0
    unique_chars = {}
    for window_end in range(len(nums)):
        right_char = nums[window_end]
        if right_char not in unique_chars:
            unique_chars[right_char] = 0
        unique_chars[right_char] += 1
        current_sum += right_char
        while window_end - window_start + 1 > len(unique_chars):
            left_char = nums[window_start]
            unique_chars[left_char] -= 1
            current_sum -= left_char
            if unique_chars[left_char] == 0:
                del unique_chars[left_char]
            window_start += 1
        max_sum = max(max_sum, current_sum)

    return max_sum


print(maximumUniqueSubarray([4, 2, 4, 5, 6]))
print(maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
