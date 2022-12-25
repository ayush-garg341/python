"""
Given a string, sort it based on the decreasing frequency of its characters.

example1:
    Input: "Programming"
    Output: "rrggmmPiano"
    Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

example2:
    Input: "abcbab"
    Output: "bbbaac"
    Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""

import heapq


def sort_character_by_frequency(string):
    max_heap = []
    freq = {}
    freq_sort = ""
    for char in string:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

    for key, val in freq.items():
        heapq.heappush(max_heap, (-val, key))

    while len(max_heap):
        top_elt = heapq.heappop(max_heap)
        freq = -top_elt[0]
        char = top_elt[1]
        for i in range(freq):
            freq_sort += char

    return freq_sort


def main():

    print(
        "String after sorting characters by frequency: "
        + sort_character_by_frequency("Programming")
    )
    print(
        "String after sorting characters by frequency: "
        + sort_character_by_frequency("abcbab")
    )


main()
