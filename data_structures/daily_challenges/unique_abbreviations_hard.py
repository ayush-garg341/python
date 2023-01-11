"""
Given a word, write a function to generate all of its unique generalized abbreviations.
"""

from collections import deque
from typing import List


def generate_generalized_abbreviation(word):
    result = []
    # TODO: Write your code here
    perms = deque()
    perms.append("")
    for i in range(len(word)):
        char = word[i]
        j = len(perms)
        while j:
            pop = list(perms.popleft())
            perms.append("".join(pop + ["_"]))
            perms.append("".join(pop + [char]))
            j -= 1

    while perms:
        pop = perms.popleft()
        s = 0
        temp = ""
        for char in pop:
            if char == "_":
                s += 1
            else:
                if s != 0:
                    temp += str(s)
                    s = 0
                temp += char
        if s != 0:
            temp += str(s)
        result.append(temp)
    return result


class Abbreviate:
    def __init__(self, str, start, count):
        self.str = str
        self.start = start
        self.count = count


def generate_generalized_abbreviation_optimized(word: str) -> List[str]:
    result = []
    perms = deque()
    perms.append(Abbreviate(list(), 0, 0))
    while perms:
        abWord = perms.popleft()
        if abWord.start == len(word):
            if abWord.count != 0:
                abWord.str.append(str(abWord.count))
            result.append("".join(abWord.str))
        else:
            perms.append(
                Abbreviate(list(abWord.str), abWord.start + 1, abWord.count + 1)
            )
            if abWord.count != 0:
                abWord.str.append(str(abWord.count))
            newWord = abWord.str
            newWord.append(word[abWord.start])
            perms.append(Abbreviate(newWord, abWord.start + 1, 0))

    return result


def unique_abb_rec(word: str):
    result = []
    unique_abb_recursive(word, list(), 0, 0, result)
    return result


def unique_abb_recursive(word, chars, start, count, result):
    if start == len(word):
        if count != 0:
            chars.append(str(count))
        result.append("".join(chars))
    else:
        unique_abb_recursive(word, list(chars), start + 1, count + 1, result)
        if count != 0:
            chars.append(str(count))
        newWord = list(chars)
        newWord.append(word[start])
        unique_abb_recursive(word, newWord, start + 1, 0, result)


def main():
    print(
        "Generalized abbreviation are: "
        + str(generate_generalized_abbreviation_optimized("system"))
    )

    print("Generalized abbreviation are: " + str(unique_abb_rec("system")))


main()
