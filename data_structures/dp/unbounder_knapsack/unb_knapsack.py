"""
Problem: Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’.
        The goal is to get the maximum profit from the items in the knapsack. We are allowed to use an unlimited quantity of an item.


ex. Items: { Apple, Orange, Melon }
    Weights: { 1, 2, 3 }
    Profits: { 15, 20, 50 }
    Capacity: 5

    5 Apples (total weight 5) => 75 profit
    1 Apple + 2 Oranges (total weight 5) => 55 profit
    2 Apples + 1 Melon (total weight 5) => 80 profit
    1 Orange + 1 Melon (total weight 5) => 70 profit

"""



def unbounded_knapsack(profits, weights, capacity):
    return recursive_brute_force(profits, weights, capacity, 0)


def recursive_brute_force(profits: list, weights: list, capacity: int, current_idx: int) -> int:
    if current_idx >= len(profits):
        return 0

    if capacity == 0:
        return 0

    profit1 = 0
    if weights[current_idx] <= capacity:
        profit1 = profits[current_idx] + recursive_brute_force(profits, weights, capacity-weights[current_idx], current_idx)

    profit2 = recursive_brute_force(profits, weights, capacity, current_idx+1)

    return max(profit1, profit2)


print("=============== brute force recursive =============== ")
print(unbounded_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(unbounded_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


def unbounded_knapsack_dp(profits, weights, capacity):
    dp = [[0 for i in range(capacity+1)] for j in range(len(weights))]
    return unbounded_knapsack_dp_top_bottom(profits, weights, capacity, dp, 0)


def unbounded_knapsack_dp_top_bottom(profits: list, weights: list, capacity: int, dp: list, current_idx: int) -> int:
    if current_idx >= len(profits):
        return 0

    if capacity == 0:
        return 0

    if dp[current_idx][capacity] == 0:
        profit1 = 0
        if weights[current_idx] <= capacity:
            profit1 = profits[current_idx] + unbounded_knapsack_dp_top_bottom(profits, weights, capacity-weights[current_idx], dp, current_idx)

        profit2 = unbounded_knapsack_dp_top_bottom(profits, weights, capacity, dp, current_idx+1)

        dp[current_idx][capacity] = max(profit1, profit2)

    return dp[current_idx][capacity]



print("=============== top down dynamic recursive =============== ")
print(unbounded_knapsack_dp([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(unbounded_knapsack_dp([15, 50, 60, 90], [1, 3, 4, 5], 6))



def unbounded_knapsack_bottom_up_tabular(profits, weights, capacity):
    n = len(profits)
    if n==0:
        return -1

    dp = [[-1 for i in range(capacity+1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i][c-weights[i]]

            if i > 0:
                profit2 = dp[i-1][c]

            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weights, profits, capacity)
    return dp[n-1][c]


def print_selected_elements(dp: list, weights: list, profits: list, capacity: int):
    n = len(weights)
    c = capacity
    total_profit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        while total_profit!=0 and total_profit != dp[i-1][c]:
            total_profit = total_profit - profits[i]
            c = capacity - weights[i]
            print(weights[i], end=" ")

    while total_profit != 0:
        total_profit = total_profit - profits[0]
        print(weights[0], end=" ")


print("=============== bottom up dynamic tabular =============== ")
print(unbounded_knapsack_bottom_up_tabular([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(unbounded_knapsack_bottom_up_tabular([15, 50, 60, 90], [1, 3, 4, 5], 6))
print(unbounded_knapsack_bottom_up_tabular([15, 20, 50], [1, 2, 3], 5))
