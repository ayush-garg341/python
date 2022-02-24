"""
Given a stair with ‘n’ steps, implement a method to count how many possible
ways are there to reach the top of the staircase, given that, at every step
you can either take 1 step, 2 steps, or 3 steps.

example1:
    Number of stairs (n) : 3
    Number of ways = 4
    Explanation: Following are the four ways we can climb : {1,1,1}, {1,2},
                                                            {2,1}, {3}

example2:
    Number of stairs (n) : 4
    Number of ways = 7
    Explanation: Following are the seven ways we can climb : {1,1,1,1},
    {1,1,2}, {1,2,1}, {2,1,1}, {2,2}, {1,3}, {3,1}
"""


def step_count_brute_force(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2

    print("calculating for n = ", n)

    return (
        step_count_brute_force(n - 1)
        + step_count_brute_force(n - 2)
        + step_count_brute_force(n - 3)
    )


print("========= step count brute force recusrive ========")
print(step_count_brute_force(3))
print(step_count_brute_force(4))
print(step_count_brute_force(5))


def step_count_dp_top_bottom(n):
    dp = [-1 for i in range(n + 1)]
    return step_count_dp_top_bottom_recursive(dp, n)


def step_count_dp_top_bottom_recursive(dp: list, n: int) -> int:

    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2

    if dp[n] == -1:
        print("calculating for n = ", n)
        dp[n] = (
            step_count_dp_top_bottom_recursive(dp, n - 1)
            + step_count_dp_top_bottom_recursive(dp, n - 2)
            + step_count_dp_top_bottom_recursive(dp, n - 3)
        )
    return dp[n]


print("========= step count dp top bottom recusrive ========")
print(step_count_dp_top_bottom(3))
print(step_count_dp_top_bottom(4))
print(step_count_dp_top_bottom(5))


def step_count_dp_bottom_up_tabular(n):
    if n == 0:
        return -1

    dp = [-1 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


print("========= step count dp bottom up tabular ========")
print(step_count_dp_bottom_up_tabular(3))
print(step_count_dp_bottom_up_tabular(4))
print(step_count_dp_bottom_up_tabular(5))
