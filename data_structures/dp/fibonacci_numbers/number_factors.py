"""
Given a number ‘n’, implement a method to count how many possible ways
there are to express ‘n’ as the sum of 1, 3, or 4.

example1:
    n : 4
    Number of ways = 4
    Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3},
                                                                    {3,1}, {4}

example2:
    n : 5
    Number of ways = 6
    Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1},
                                        {1,1,3}, {1,3,1}, {3,1,1}, {1,4}, {4,1}
"""


def count_ways_brute_force_recursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    print("calculating for n = ", n)
    return (
        count_ways_brute_force_recursive(n - 1)
        + count_ways_brute_force_recursive(n - 3)
        + count_ways_brute_force_recursive(n - 4)
    )


print("======== count ways brute force recusrive ==========")
print(count_ways_brute_force_recursive(4))
print(count_ways_brute_force_recursive(5))
print(count_ways_brute_force_recursive(6))
print(count_ways_brute_force_recursive(10))


def count_ways_dp_top_bottom(n):
    dp = [-1 for i in range(n + 1)]
    return count_ways_dp_top_bottom_recursive(dp, n)


def count_ways_dp_top_bottom_recursive(dp: list, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    if dp[n] == -1:
        print("calculating for n = ", n)
        dp[n] = (
            count_ways_dp_top_bottom_recursive(dp, n - 1)
            + count_ways_dp_top_bottom_recursive(dp, n - 3)
            + count_ways_dp_top_bottom_recursive(dp, n - 4)
        )

    return dp[n]


print("======== count ways dp bottom recursive ==========")
print(count_ways_dp_top_bottom(4))
print(count_ways_dp_top_bottom(5))
print(count_ways_dp_top_bottom(6))
print(count_ways_dp_top_bottom(10))


def count_ways_dp_bottom_up_tabular(n):
    if n == 0:
        return -1

    dp = [-1 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        print("calculating for n = ", i)
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

    return dp[n]


print("======== count ways dp bottom up tabualr ==========")
print(count_ways_dp_bottom_up_tabular(4))
print(count_ways_dp_bottom_up_tabular(5))
print(count_ways_dp_bottom_up_tabular(6))
print(count_ways_dp_bottom_up_tabular(10))
