"""
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

example1:
    Input: "aappp"
    Output: "papap"
    Explanation: In "papap", none of the repeating characters come next to each other.

example2:
    Input: "Programming"
    Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
    Explanation: None of the repeating characters come next to each other.

example3:
    Input: "aapa"
    Output: ""
    Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
"""

import heapq


def rearrange_string(string):
    # TODO: Write your code here
    freq_map = {}
    for char in string:
        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1

    max_heap = []
    for key, val in freq_map.items():
        # Pusing based on frequency of char
        heapq.heappush(max_heap, (-val, key))

    result_string = []
    previous_char, previous_freq = None, 0
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        if previous_char and -previous_freq > 0:
            heapq.heappush(max_heap, (previous_freq, previous_char))

        result_string.append(char)
        previous_char = char
        previous_freq = freq + 1

    return "".join(result_string) if len(result_string) == len(string) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
