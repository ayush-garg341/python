"""
You're given two positive integers i.e. width and height of a grid shaped, rectangular graph.
Write a function to determine number of ways to reach the bottom of the graph.

example1. width = 2, height = 3
    1. down, down, right
    2. down, right, down
    3. right, down, down
"""


def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    return number_of_ways_rec(width - 1, height - 1)


def number_of_ways_rec(right_most, bottom_most):
    if right_most < 0 or bottom_most < 0:
        return 0
    if right_most == 0 and bottom_most == 0:
        return 1

    count1 = number_of_ways_rec(right_most - 1, bottom_most)
    count2 = number_of_ways_rec(right_most, bottom_most - 1)

    return count1 + count2


print(numberOfWaysToTraverseGraph(2, 3))
print(numberOfWaysToTraverseGraph(3, 3))
print(numberOfWaysToTraverseGraph(4, 3))
print(numberOfWaysToTraverseGraph(5, 5))


def numberOfWaysToTraverseGraph_dp_rec(width, height):
    dp = [[0 for i in range(height)] for j in range(width)]
    return number_of_ways_rec_dp(width - 1, height - 1, dp)


def number_of_ways_rec_dp(right_most, bottom_most, dp):
    if right_most < 0 or bottom_most < 0:
        return 0

    if right_most == 0 and bottom_most == 0:
        return 1

    if dp[right_most][bottom_most] != 0:
        return dp[right_most][bottom_most]

    count1 = number_of_ways_rec_dp(right_most - 1, bottom_most, dp)
    count2 = number_of_ways_rec_dp(right_most, bottom_most - 1, dp)

    dp[right_most][bottom_most] = count1 + count2

    return dp[right_most][bottom_most]


print("using dp")

print(numberOfWaysToTraverseGraph_dp_rec(2, 3))
print(numberOfWaysToTraverseGraph_dp_rec(3, 3))
print(numberOfWaysToTraverseGraph_dp_rec(4, 3))
print(numberOfWaysToTraverseGraph_dp_rec(5, 5))


def traversal_ways_tabular(width, height):
    dp = [[0 for i in range(width)] for j in range(height)]

    for i in range(1, width):
        dp[0][i] = 1

    for j in range(1, height):
        dp[j][0] = 1

    for row in range(1, height):
        for col in range(1, width):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[height - 1][width - 1]


print("Using dp tabular")

print(traversal_ways_tabular(2, 3))
print(traversal_ways_tabular(3, 3))
print(traversal_ways_tabular(4, 3))
print(traversal_ways_tabular(5, 5))
