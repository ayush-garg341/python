"""
Given two strings, str1 and str2, check whether str2 is an anagram of str1.
An anagram is a word or phrase created by rearranging the letters of another
word or phrase. while utilizing each of the original letters exactly once.
"""


def is_anagram(str1, str2):
    char_map = dict()
    for char in str2:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    for char in str1:
        if char in char_map:
            char_map[char] -= 1
            if char_map[char] == 0:
                del char_map[char]
        else:
            return False
    if len(char_map.keys()):
        return False
    return True


print(is_anagram("creative", "reactive"))
print(is_anagram("ram", "car"))
