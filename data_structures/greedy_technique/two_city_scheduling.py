"""
Given cost of two cities, a and b, invite 50% of people to a and 50% to b while minimizing the cost.
"""


def two_city_scheduling(costs):
    n = len(costs)
    total_cost = 0
    costs.sort(key=lambda x: x[0] - x[1])
    print(costs)
    for i in range(n):
        if i < n // 2:
            total_cost += costs[i][0]
        else:
            total_cost += costs[i][1]
    return total_cost
