"""
input -> "python is my fav language"
output -> "language fav my is python"
"""


def reverse_words_in_string(string):
    reverse_string = ""

    n = len(string)

    print("len of original string is : ", n)

    for i in range(n-1, -1, -1):
        reverse_string += string[i]

    print("len of reversed string is : ", len(reverse_string))

    reverse_word_by_word = ""

    start = -1
    end = -1
    white_space = True

    for j in range(n):
        if reverse_string[j] != " ":
            end += 1
            white_space = False
        else:
            if not white_space:
                for char in range(end, start, -1):
                    reverse_word_by_word += reverse_string[char]
            white_space = True
            reverse_word_by_word += " "
            start = j
            end = j

    if not white_space:
        for char in range(end, start, -1):
            reverse_word_by_word += reverse_string[char]

    print("reverse word by word : ", len(reverse_word_by_word))

    return reverse_word_by_word

inp = "python is my fav language"
print(reverse_words_in_string(inp))

inp2 = "I love c  "
print(reverse_words_in_string(inp2))

inp3 = "  I hate JS  "
print(reverse_words_in_string(inp3))
