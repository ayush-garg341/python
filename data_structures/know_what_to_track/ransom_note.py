"""
Given two strings, ransom_note and magazine, check if ransom_note
can be constructed using the letters from magazine.

Return TRUE if it can be constructed, FALSE otherwise.
"""


def can_construct(ransom_note, magazine):
    # Replace this placeholder return statement with your code
    magazine_dict = dict()
    for char in magazine:
        if char not in magazine_dict:
            magazine_dict[char] = 0
        magazine_dict[char] += 1

    for char in ransom_note:
        if char in magazine_dict:
            magazine_dict[char] -= 1
            if magazine_dict[char] == 0:
                del magazine_dict[char]
        else:
            return False
    return True
