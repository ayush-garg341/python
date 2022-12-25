"""
Given a set of investment projects with their respective profits, we need to find the most profitable projects.
We are given an initial capital and are allowed to invest only in a fixed number of projects.
Our goal is to choose projects that give us the maximum profit.

example1:
    Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
    Output: 6
    Explanation:
        1. With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’.
            Once we selected our first project, our total capital will become 3 (profit + initial capital).
        2. With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.

        After the completion of the two projects, our total capital will be 6 (1+2+3).
"""

import heapq


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    min_capital_heap = []
    max_profit_heap = []

    available_capital = initialCapital

    for i in range(len(capital)):
        heapq.heappush(min_capital_heap, (capital[i], i))

    for _ in range(numberOfProjects):
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            min_cap = heapq.heappop(min_capital_heap)
            idx = min_cap[1]
            heapq.heappush(max_profit_heap, (-profits[idx], idx))

        if not max_profit_heap:
            break
        available_capital += -heapq.heappop(max_profit_heap)[0]
    return available_capital


def main():

    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print(
        "Maximum capital: "
        + str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0))
    )


main()
