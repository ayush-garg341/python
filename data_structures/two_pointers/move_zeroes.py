from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        # Your code goes here
        first_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0 and first_zero == -1:
                first_zero = i
            elif nums[i] != 0:
                if first_zero != -1 and i > first_zero:
                    nums[i], nums[first_zero] = nums[first_zero], nums[i]
                    first_zero += 1
