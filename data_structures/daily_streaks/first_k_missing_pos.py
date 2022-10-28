"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
"""

def find_first_k_missing_positive(nums, k):
    result = []
    i, n = 0, len(nums)
    while i < n:
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
            idx = nums[i] - 1
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1

    number_present = set()
    for i in range(len(nums)):
        if nums[i] != i+1:
            result.append(i+1)
            if len(result) == k:
                return result
            number_present.add(nums[i])

    left = k - len(result)
    greatest_so_far = n
    while left > 0:
        greatest_so_far += 1
        if greatest_so_far not in number_present:
            result.append(greatest_so_far)
            left -= 1

    return result

print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
print(find_first_k_missing_positive([2, 3, 4], 3))
print(find_first_k_missing_positive([-2, -3, 4], 2))
print(find_first_k_missing_positive([-2, -3, 7], 4))



