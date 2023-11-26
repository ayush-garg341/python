"""
Starting point of gas station so that can reach again at same point.
Given gas available and cost to reach from one station to next.
"""


def gas_station_journey(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    current_gas, start_idx = 0, 0
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            current_gas = 0
            start_idx = i + 1

    return start_idx
