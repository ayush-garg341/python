"""
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters
are at least ‘K’ distance apart from each other.

example1:
    Input: "mmpp", K=2
    Output: "mpmp" or "pmpm"
    Explanation: All same characters are 2 distance apart.

example2:
    Input: "Programming", K=3
    Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
    Explanation: All same characters are 3 distance apart.

example3:
    Input: "aab", K=2
    Output: "aba"
    Explanation: All same characters are 2 distance apart.

example4:
    Input: "aappa", K=3
    Output: ""
    Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
"""

import heapq
from collections import deque


def reorganize_string(string, k):
    # TODO: Write your code here
    freq_map = {}
    for char in string:
        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1

    max_heap = []
    for key, val in freq_map.items():
        heapq.heappush(max_heap, (-val, key))

    result_string = []
    queue = deque()
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result_string.append(char)
        queue.append((char, freq + 1))
        if len(queue) == k:
            char, freq = queue.popleft()
            if -freq > 0:
                heapq.heappush(max_heap, (freq, char))

    return "".join(result_string) if len(result_string) == len(string) else ""


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
