"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all the words.

example 1:
    input - ["this", "that", "did", "deed", "them!", "a"]
    output - ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]

explanation -> the first word "this", will require t, h, i, s but second word "that" will require one extra t, a since
            one t and h we already have.
"""


def minimumCharactersForWords(words):
    # Write your code here.
    unique_words_dict = {}
    result = []
    for word in words:
        word_char_freq = {}
        for char in word:
            word_char_freq[char] = word_char_freq.get(char, 0) + 1
        for key, val in word_char_freq.items():
            if key not in unique_words_dict or unique_words_dict[key] < val:
                unique_words_dict[key] = val
    for char, count in unique_words_dict.items():
        for i in range(count):
            result.append(char)
    return result


def minimumCharactersForWordsEfficient(words):
    # Write your code here.
    unique_letters_map = {}
    result = []
    for word in words:
        word_char_map = {}
        for char in word:
            if char not in unique_letters_map:
                unique_letters_map[char] = 1
                result.append(char)
            word_char_map[char] = word_char_map.get(char, 0) + 1
            if word_char_map[char] > unique_letters_map[char]:
                result.append(char)
                unique_letters_map[char] += 1

    return result


print(minimumCharactersForWordsEfficient(["this", "that", "did", "deed", "them!", "a"]))
