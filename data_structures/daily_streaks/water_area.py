"""
Given an input array of non-negative integers where each integer represents the height of pillar with width 1.
Write a function that returns the surface area of water trapped between pillars.

Hint: At any index we can store the max water = min(left_max, right_max) of that index.
"""


def waterArea(heights):
    # Write your code here.
    right_max = [-1] * len(heights)
    left_max = [-1] * len(heights)

    max_left = -1
    for i in range(len(heights)):
        if heights[i] > max_left:
            max_left = heights[i]
        left_max[i] = max_left

    max_right = -1
    for j in range(len(heights) - 1, -1, -1):
        if heights[j] > max_right:
            max_right = heights[j]
        right_max[j] = max_right

    max_water = 0
    for i in range(len(heights)):
        max_water += min(left_max[i], right_max[i]) - heights[i]

    return max_water


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))


def waterAreaSpaceEff(heights):
    # Write your code here.
    dp = [-1] * len(heights)
    left_max = -1
    for i in range(len(heights)):
        if heights[i] > left_max:
            left_max = heights[i]
        dp[i] = left_max

    right_max = -1
    for j in range(len(heights) - 1, -1, -1):
        if heights[j] > right_max:
            right_max = heights[j]

        dp[j] = min(dp[j], right_max)

    max_water = 0
    for i in range(len(heights)):
        max_water += dp[i] - heights[i]

    return max_water


print(waterAreaSpaceEff([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))


def waterAreaConstantSpace(heights):
    left = 0
    right = len(heights) - 1
    left_max = -1
    right_max = -1
    water_area = 0
    while left < right:
        left_max = max(left_max, heights[left])
        right_max = max(right_max, heights[right])
        if left_max < right_max:
            water_area += left_max - heights[left]
            left += 1
        else:
            water_area += right_max - heights[right]
            right -= 1

    return water_area


print(waterAreaConstantSpace([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
