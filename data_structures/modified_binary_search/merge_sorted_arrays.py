"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

example1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

example2:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    count_1 = m - 1
    count_2 = n - 1
    last = m + n - 1
    print(count_1, count_2)
    while count_1 >= 0 and count_2 >= 0:
        if nums1[count_1] > nums2[count_2]:
            nums1[last] = nums1[count_1]
            count_1 -= 1
        else:
            nums1[last] = nums2[count_2]
            count_2 -= 1
        last -= 1

    while count_1 >= 0:
        nums1[last] = nums1[count_1]
        last -= 1
        count_1 -= 1

    while count_2 >= 0:
        nums1[last] = nums2[count_2]
        last -= 1
        count_2 -= 1

    return nums1


# print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([0], 0, [1], 1))
