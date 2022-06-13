"""
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are
on index i on the current row, you may move to either index i or index i + 1 on the next row.

example1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
       2
      3 4
     6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

example2:
    Input: triangle = [[-10]]
    Output: -10
"""

from typing import List
import math


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> float:
        # max_row_len = len(triangle[-1])
        dp = []
        for row in triangle:
            elt_list = []
            for elt in row:
                elt_list.append(math.inf)
            dp.append(elt_list)
        # dp = [[math.inf for i in range(max_row_len)] for j in range(max_row_len)]
        return self.minimumTotalRec(triangle, dp, 0, 0)

    def minimumTotalRec(self, triangle, dp, row_index, elt_index) -> float:
        if row_index >= len(triangle):
            return 0
        if elt_index >= len(triangle[row_index]):
            return 0

        if dp[row_index][elt_index] != math.inf:
            return dp[row_index][elt_index]
        else:
            sum1, sum2 = 0, 0
            sum1 += triangle[row_index][elt_index] + self.minimumTotalRec(triangle, dp, row_index + 1, elt_index)

            if elt_index + 1 < len(triangle[row_index]):
                sum2 += triangle[row_index][elt_index + 1] + self.minimumTotalRec(
                    triangle, dp, row_index + 1, elt_index + 1
                )
            else:
                sum2 = math.inf
            dp[row_index][elt_index] = min(sum1, sum2)
        return dp[row_index][elt_index]


soln = Solution()

print(soln.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(soln.minimumTotal([[-10]]))
print(soln.minimumTotal([[-1], [2, 3], [1, -1, -3]]))
