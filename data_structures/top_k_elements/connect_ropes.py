"""
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
The cost of connecting two ropes is equal to the sum of their lengths.

example1:
    Input: [1, 3, 11, 5]
    Output: 33
    Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

example2:
    Input: [3, 4, 5, 6]
    Output: 36
    Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

example3:
    Input: [1, 3, 11, 5, 2]
    Output: 42
    Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
"""

import heapq


def minimum_cost_to_connect_ropes(ropeLengths):
    if len(ropeLengths) == 1:
        return ropeLengths[0]
    if len(ropeLengths) == 2:
        return ropeLengths[0] + ropeLengths[1]
    min_heap = []
    for length in ropeLengths:
        heapq.heappush(min_heap, length)

    temp, result = 0, 0

    while len(min_heap) != 1:
        first_min = heapq.heappop(min_heap)
        second_min = heapq.heappop(min_heap)
        temp = first_min + second_min
        result += first_min + second_min
        heapq.heappush(min_heap, temp)

    return result


def main():

    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
