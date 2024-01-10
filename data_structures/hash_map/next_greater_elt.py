"""
for each element x in nums1, find the next greater element
present on the right side of x in nums2 and store it in the ans array.
"""


def next_greater_element(nums1, nums2):
    stack = []
    next_greater = dict()
    for num in nums2:
        if len(stack) == 0:
            stack.append(num)
        else:
            while len(stack) and num > stack[-1]:
                top = stack.pop()
                next_greater[top] = num
            stack.append(num)

    for i in range(len(nums1)):
        current_element = nums1[i]
        if current_element in next_greater.keys():
            nums1[i] = next_greater[current_element]
        else:
            nums1[i] = -1

    return nums1


print(next_greater_element([5, 4, 7], [4, 5, 7, 3]))
print(next_greater_element([9, 7, 6], [5, 7, 6, 8, 9]))
