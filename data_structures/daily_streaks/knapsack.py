"""
Given an array of items containing value and weight. Given a capacity determine the max value.
"""
def knapsackProblem(items, capacity):
    dp = [[0 for i in range(capacity + 1)] for j in range(len(items)+1)]


    for i in range(1, len(items)+1):
        for c in range(1, capacity+1):
            j = i - 1
            if items[j][1] <= c:
                dp[i][c] = max(dp[i-1][c], items[j][0] + dp[i-1][c-items[j][1]])
            else:
                dp[i][c] = dp[i-1][c]

    rows = len(dp) - 1
    cols = len(dp[0]) - 1
    elts = []
    print_selected_elements(dp, elts, items, capacity)
    elts.reverse()
    return [dp[len(items)][capacity], elts]


def print_selected_elements(dp, elts, items, capacity):
    n = len(items)
    total_profit = dp[n][capacity]
    for i in range(n, 0, -1):
        j = i - 1
        if total_profit!=0 and total_profit!=dp[i-1][capacity]:
            capacity = capacity - items[j][1]
            total_profit = total_profit - items[j][0]
            elts.append(j)


capacity = 200
items = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
  ]

print(knapsackProblem(items, capacity))
