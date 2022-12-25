"""
    Maximize the profit by putting items in knapsack of capacity C.
    Items: { Apple, Orange, Banana, Melon }
    Weights: { 2, 3, 1, 4 }
    Profits: { 4, 5, 3, 7 }
    Knapsack capacity: 5

    Max profit = 10 by putting Banana and Melon -> 4+1 = 5
"""


# Very basic recursive solution to the problem


def max_profit(weights, profits, capacity):
    profit = -1
    current_idx = 0
    profit = max_profit_recursive(weights, profits, capacity, current_idx)
    return profit


def max_profit_recursive(weights, profits, capacity, current_idx):
    if capacity <= 0 or current_idx >= len(profits):
        return 0

    profit1 = 0
    if weights[current_idx] <= capacity:
        profit1 = profits[current_idx] + max_profit_recursive(
            weights, profits, capacity - weights[current_idx], current_idx + 1
        )

    profit2 = max_profit_recursive(weights, profits, capacity, current_idx + 1)

    return max(profit1, profit2)


capacity = 7
profit = max_profit([1, 2, 3, 5], [1, 6, 10, 16], capacity)
print(profit)

capacity = 6
profit = max_profit([1, 2, 3, 5], [1, 6, 10, 16], capacity)
print(profit)


def knapsack_recursive_with_memoization(weights, profits, capacity):
    """
    Top down recursive approach with memoization
    """
    dp = [[-1 for i in range(capacity + 1)] for j in range(len(profits))]
    current_idx = 0
    profit = knapsack_recursive(weights, profits, dp, capacity, current_idx)
    return profit


def knapsack_recursive(weights, profits, dp, capacity, current_idx):
    if capacity <= 0 or current_idx >= len(profits):
        return 0

    if dp[current_idx][capacity] != -1:
        return dp[current_idx][capacity]

    profit1 = 0
    if weights[current_idx] <= capacity:
        profit1 = profits[current_idx] + max_profit_recursive(
            weights, profits, capacity - weights[current_idx], current_idx + 1
        )

    profit2 = max_profit_recursive(weights, profits, capacity, current_idx + 1)

    dp[current_idx][capacity] = max(profit1, profit2)
    return dp[current_idx][capacity]


capacity = 7
profit = knapsack_recursive_with_memoization([1, 2, 3, 5], [1, 6, 10, 16], capacity)
print(profit)

capacity = 6
profit = knapsack_recursive_with_memoization([1, 2, 3, 5], [1, 6, 10, 16], capacity)
print(profit)


def knapsack_bottom_up_tabular(weights, profits, capacity):
    """
    Tabular approach bottoms-up for solving knapsack problem
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for i in range(capacity + 1)] for j in range(len(profits))]
    for c in range(capacity + 1):
        dp[0][c] = profits[0]
    dp[0][0] = 0
    for i in range(1, len(profits)):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            # include the current weight
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]

            # exclude the current weight
            profit2 = dp[i - 1][c]
            dp[i][c] = max(profit1, profit2)

    print("selected elements are :")
    print_selected_elements(dp, profits, weights, capacity)
    print("")
    return dp[len(profits) - 1][capacity]


def print_selected_elements(dp, profits, weights, capacity):
    """
    Print selected elements in knapsack
    range(start, stop, step)
        ex. range(5, 0, -1)
            5, 4, 3, 2, 1
    """
    n = len(weights)
    total_profit = dp[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if total_profit != 0 and total_profit != dp[i - 1][capacity]:
            capacity = capacity - weights[i]
            total_profit = total_profit - profits[i]
            print(weights[i], end=" ")

    if total_profit != 0:
        print(weights[0], end=" ")


capacity = 7
profit = knapsack_bottom_up_tabular([1, 2, 3, 5], [1, 6, 10, 16], capacity)
print(profit)

capacity = 6
profit = knapsack_bottom_up_tabular([1, 2, 3, 5], [1, 6, 10, 16], capacity)
print(profit)


def knapsack_bottom_up_tabular_mem_efficient(weights, profits, capacity):
    """
    Memory efficient version of tabular bottom-up approach.
    Does the job in mem space O(C)
    independent of number of elements.
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for i in range(capacity + 1)] for j in range(2)]
    for c in range(capacity + 1):
        dp[0][c] = profits[0]
    dp[0][0] = 0
    for i in range(1, len(profits)):
        for c in range(1, capacity + 1):
            indx = i % 2
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[indx - 1][c - weights[i]]

            profit2 = dp[indx - 1][c]

            dp[indx][c] = max(profit1, profit2)

    return dp[(n - 1) % 2][capacity]


capacity = 7
profit = knapsack_bottom_up_tabular_mem_efficient(
    [1, 2, 3, 5], [1, 6, 10, 16], capacity
)
print(profit)

capacity = 6
profit = knapsack_bottom_up_tabular_mem_efficient(
    [1, 2, 3, 5], [1, 6, 10, 16], capacity
)
print(profit)
