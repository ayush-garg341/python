"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order

example1:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
     [1,2,1],
     [2,1,1]]
"""

from collections import deque
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 0:
            return result
        nums.sort()
        unique_per = set()
        permutations = deque()
        permutations.append([])
        for current_num in nums:
            n = len(permutations)
            for _ in range(n):
                old_per = permutations.popleft()
                for i in range(len(old_per) + 1):
                    new_per = list(old_per)
                    new_per.insert(i, current_num)
                    unique_str = "-".join(str(num) for num in new_per)
                    if unique_str not in unique_per:
                        if len(new_per) == len(nums):
                            result.append(new_per)
                        else:
                            permutations.append(new_per)
                        unique_per.add(unique_str)
        return result


soln = Solution()
print(soln.permuteUnique([1, 1, 2]))
