"""
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
find the length of the longest substring having the same letters after replacement.

example1:
    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

example2:
    Input: String="abbcb", k=1
    Output: 4
    Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

Why don’t we need to update this max_repeating_letter when we shrink the window? Since we have to replace all the
remaining letters to get the longest substring having the same letter in any window, we can’t get a better answer from
any other window even though all occurrences of the letter with frequency maxRepeatLetterCount is not in the current
window.
"""


def longest_substr_same_letters_after_replacement(string: str, k: int) -> int:
    max_len = 0
    window_start = 0

    distinct = {}
    max_repeating_letter = 0
    for window_end in range(len(string)):
        char = string[window_end]
        if char not in distinct:
            distinct[char] = 0
        distinct[char] += 1
        max_repeating_letter = max(
            max_repeating_letter, distinct[char]
        )  # do we need to update this while shrinking
        remaining_letters = window_end - window_start + 1 - max_repeating_letter

        while remaining_letters > k:
            left_char = string[window_start]
            distinct[left_char] -= 1
            if distinct[left_char] == 0:
                del distinct[left_char]
            window_start += 1
            remaining_letters = window_end - window_start + 1 - max_repeating_letter
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


print(longest_substr_same_letters_after_replacement("aabccbb", 2))
print(longest_substr_same_letters_after_replacement("abbcb", 1))
print(longest_substr_same_letters_after_replacement("abccde", 1))
print(longest_substr_same_letters_after_replacement("abcd", 2))
