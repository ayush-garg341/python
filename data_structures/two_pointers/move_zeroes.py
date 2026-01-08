from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        # Your code goes here
        # Check where is first 0
        first_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                first_zero = i
                break

        for i in range(len(nums)):
            # Swap any non-zero element with the first zero index.
            if nums[i] != 0:
                if first_zero != -1 and i > first_zero:
                    nums[i], nums[first_zero] = nums[first_zero], nums[i]
                    first_zero += 1
