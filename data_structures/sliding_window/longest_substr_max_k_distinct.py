"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

example1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

example2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".
"""


def longest_substr_max_k_distinct(string: str, k: int) -> int:
    window_start = 0
    length = 0
    distinct = {}
    for window_end in range(len(string)):
        char = string[window_end]
        if char not in distinct:
            distinct[char] = 0
        distinct[char] += 1

        while len(distinct) > k:
            left_char = string[window_start]
            distinct[left_char] -= 1
            if distinct[left_char] == 0:
                del distinct[left_char]
            window_start += 1
        length = max(length, window_end - window_start + 1)

    return length


print(longest_substr_max_k_distinct("araaci", 2))
print(longest_substr_max_k_distinct("araaci", 1))
print(longest_substr_max_k_distinct("cbbebi", 3))
print(longest_substr_max_k_distinct("cbbebi", 10))
print(longest_substr_max_k_distinct("eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh", 16))
