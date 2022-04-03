"""
The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as
many fruits as possible to be placed in the given baskets.

example1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

example2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
    This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

This problem follows longest substr with max k distinct char pattern, where k = 2
"""


def fruits_into_baskets(fruits: list) -> int:
    k = 2
    window_start = 0
    max_len = 0
    distinct = {}
    for window_end in range(len(fruits)):
        char = fruits[window_end]
        if char not in distinct:
            distinct[char] = 0
        distinct[char] += 1

        while len(distinct) > k:
            left_char = fruits[window_start]
            distinct[left_char] -= 1
            if distinct[left_char] == 0:
                del distinct[left_char]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


print(fruits_into_baskets(["A", "B", "C", "A", "C"]))
print(fruits_into_baskets(["A", "B", "C", "B", "B", "C"]))
