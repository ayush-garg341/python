"""
Given an array of strings and each element in the array has a length of two.
You need to return the length of the longest palindrome that can be made by
concatenating some elements.
If no palindrome can be made, return 0.
"""

from collections import defaultdict


def longest_palindrome(words):
    longest = 0
    palindrome_words_odd_freq = 0
    freq_dict = defaultdict(int)
    for word in words:
        freq_dict[word] += 1
    print(freq_dict)
    for word, freq in freq_dict.items():
        if word[0] == word[1]:
            # Check if the word is palindrome
            longest += freq if freq % 2 == 0 else freq - 1
            if freq % 2 == 1:
                palindrome_words_odd_freq += 1
        else:
            # if word is not palindrome
            if word[1] > word[0]:
                reverse = word[1] + word[0]
                # Do not process the word again which is already processed
                if reverse in freq_dict:
                    freq_2 = freq_dict[reverse]
                    longest += min(freq, freq_2) * 2
    if palindrome_words_odd_freq:
        longest += 1

    return longest * 2


print(longest_palindrome(["aa", "bb", "aa", "bb", "aa", "bb"]))
print(longest_palindrome(["aa", "bb", "aa", "ea"]))
print(longest_palindrome(["aa", "bb", "cc", "dd"]))
print(longest_palindrome(["ab", "cd", "ef", "gh", "ij"]))
print(longest_palindrome(["ab", "bc", "ca", "da", "ed"]))
