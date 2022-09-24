"""
Calculate the max sum of strictly increasing subseq in an array and alsp return the elements.
"""

import math
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    max_sum_at_each_index = [(-math.inf, -1)] * len(array)
    prev_idx = -1
    global_max = -math.inf
    global_max_idx = -1
    elts = []
    for start in range(len(array)):
        sum = array[start]
        for end in range(start-1, -1, -1):
            if array[end] < array[start]:
                if max_sum_at_each_index[end][0] + array[start] > sum:
                    sum = max_sum_at_each_index[end][0] + array[start]
                    prev_idx = end
        max_sum_at_each_index[start] = (sum, prev_idx)
        if sum > global_max:
            global_max = sum
            global_max_idx = start

    elts.append(array[global_max_idx])
    prev_idx = max_sum_at_each_index[global_max_idx][1]
    while prev_idx != -1:
        elts.append(array[prev_idx])
        prev_idx = max_sum_at_each_index[prev_idx][1]

    elts.reverse()

    return [global_max, elts]

print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
