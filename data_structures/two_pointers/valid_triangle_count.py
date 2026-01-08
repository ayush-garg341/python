from typing import List


class Solution:
    def triangleNumber(self, heights: List[int]):
        # Your code goes here
        heights.sort()
        count = 0
        for i in range(len(heights) - 1, -1, -1):
            left = 0
            right = i - 1
            while left < right:
                if heights[left] + heights[right] > heights[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count


sol = Solution()
print(sol.triangleNumber([1, 2, 3, 4]))
