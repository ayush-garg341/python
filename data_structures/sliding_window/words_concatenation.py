"""
Given a string and a list of words, find all the starting indices of substrings in the given string that are a
concatenation of all the given words exactly once without any overlapping of words.

example1:
    Input: String="catfoxcat", Words=["cat", "fox"]
    Output: [0, 3]
    Explanation: The two substring containing both the words are "catfox" & "foxcat".

example2:
    Input: String="catcatfoxfox", Words=["cat", "fox"]
    Output: [3]
    Explanation: The only substring containing both the words is "catfox".
"""


def find_word_concatenation(str1, words):
    result_indices = []
    window_start = 0
    matched = 0
    pattern_len = len(words[0]) * len(words)
    char_freq = {}
    for word in words:
        for char in word:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        if matched == len(char_freq):
            substr = str1[window_start : window_end + 1]
            flag = True
            for word in words:
                if word in substr:
                    continue
                else:
                    flag = False
            if flag is True:
                result_indices.append(window_start)

        if window_end >= pattern_len - 1:
            left_char = str1[window_start]
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

            window_start += 1

    return result_indices


print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
print(find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(find_word_concatenation("barfoothefoobarman", ["foo", "bar"]))
