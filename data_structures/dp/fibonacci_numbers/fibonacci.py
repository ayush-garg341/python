"""
Write a function to calculate the nth Fibonacci number.
Fibonacci numbers are a series of numbers in which each number is the sum
of the two preceding numbers.

First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …
"""


def fibonacci_brute_force(n):
    if n < 2:
        return n
    return fibonacci_brute_force(n - 1) + fibonacci_brute_force(n - 2)


print("====== fibonacci brute force =======")
print(fibonacci_brute_force(2))
print(fibonacci_brute_force(5))


def fibonacci_dp_top_bottom(n):
    dp = [None for i in range(n + 1)]
    return fibonacci_dp_top_bottom_recursive(dp, n)


def fibonacci_dp_top_bottom_recursive(dp: list, n: int) -> int:
    if n < 2:
        return n

    if dp[n] == None:
        dp[n] = fibonacci_dp_top_bottom_recursive(
            dp, n - 1
        ) + fibonacci_dp_top_bottom_recursive(dp, n - 2)

    return dp[n]


print("====== fibonacci dp top bottom recursive =======")
print(fibonacci_dp_top_bottom(2))
print(fibonacci_dp_top_bottom(5))


def fibonacci_dp_bottom_up_tabular(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print("====== fibonacci bottom up tabular =======")
print(fibonacci_dp_bottom_up_tabular(2))
print(fibonacci_dp_bottom_up_tabular(5))


def fibonacci_dp_bottom_up_tabular_mem_optimize(n):
    dp = []
    dp.append(0)
    dp.append(1)
    for i in range(2, n + 1):
        dp[i % 2] = dp[0] + dp[1]

    return dp[n % 2]


print("====== fibonacci bottom up tabular memory optimize =======")
print(fibonacci_dp_bottom_up_tabular_mem_optimize(2))
print(fibonacci_dp_bottom_up_tabular_mem_optimize(5))
