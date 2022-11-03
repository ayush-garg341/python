"""
Move all zeros to the end while maintaining relative order of non-zero elements.
"""

def move_zeros(nums):
    zeroth_pos = -1
    i = 0
    while i < len(nums):
        if nums[i]!=0:
            if zeroth_pos != -1:
                nums[zeroth_pos], nums[i] = nums[i], nums[zeroth_pos]
                zeroth_pos += 1
        else:
            if zeroth_pos == -1:
                zeroth_pos = i
        i += 1
    return nums

print(move_zeros([0, 1, 0, 3, 12]))
