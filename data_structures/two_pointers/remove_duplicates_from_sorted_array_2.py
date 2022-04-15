"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each
unique element appears at most twice. The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.

example1:
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

example2:
    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def remove_duplicates(nums) -> int:
    start = 0
    count = 1
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[start]:
            if count < 2:
                count += 1
                start += 1
                nums[start] = nums[i]
        else:
            start += 1
            nums[start] = nums[i]
            count = 1

    print(nums)

    return start + 1


print(remove_duplicates([1, 1, 1, 2, 2, 3]))
print(remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
