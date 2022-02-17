"""
    Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit.
    We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

ex. 1
    Lengths: [1, 2, 3, 4, 5]
    Prices: [2, 6, 7, 10, 13]
    Rod Length: 5

    Five pieces of length 1 => 10 price
    Two pieces of length 2 and one piece of length 1 => 14 price
    One piece of length 3 and two pieces of length 1 => 11 price
    One piece of length 3 and one piece of length 2 => 13 price
    One piece of length 4 and one piece of length 1 => 12 price
    One piece of length 5 => 13 price
"""


def max_profit(lengths: list, prices: list, rod_len: int):
    if len(lengths) != len(prices):
        return -1
    if len(lengths) == 0 or len(prices) == 0:
        return -1
    return max_profit_brute_force_recursive(lengths, prices, rod_len, 0)


def max_profit_brute_force_recursive(lengths: list, prices: list, rod_len: int, current_idx: int):
    if current_idx >= len(prices):
        return 0

    if rod_len == 0:
        return 0

    profit1 = 0
    if lengths[current_idx] <= rod_len:
        profit1 += prices[current_idx] + max_profit_brute_force_recursive(lengths, prices, rod_len-lengths[current_idx], current_idx)

    profit2 = max_profit_brute_force_recursive(lengths, prices, rod_len, current_idx+1)

    return max(profit1, profit2)


print("==================== brute force recursive ==================")
print(max_profit([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


def max_profit_dp_top_bottom(lengths, prices, rod_len):
    dp = [[-1 for i in range(rod_len+1)] for j in range(len(prices))]
    return max_profit_dp_recursive(lengths, prices, rod_len, dp, 0)

def max_profit_dp_recursive(lengths: list, prices: list, rod_len: list, dp: list, current_idx: int):
    if current_idx >= len(prices):
        return 0

    if rod_len == 0:
        return 0

    if dp[current_idx][rod_len] == -1:
        profit1 = 0
        if lengths[current_idx] <= rod_len:
            profit1 = prices[current_idx] + max_profit_dp_recursive(lengths, prices, rod_len-lengths[current_idx], dp, current_idx)

        profit2 = max_profit_dp_recursive(lengths, prices, rod_len, dp, current_idx+1)

        dp[current_idx][rod_len] = max(profit1, profit2)

    return dp[current_idx][rod_len]


print("==================== dp top bottom recursive ==================")
print(max_profit_dp_top_bottom([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


"""
Same tabular bottom up solution can be implemented as in case of unbounded knapsack.
"""
