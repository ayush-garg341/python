"""
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

example1:
    Input: str1="xy#z", str2="xzz#"
    Output: true
    Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

example2:
    Input: str1="xy#z", str2="xyz#"
    Output: false
    Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

example3:
    Input: str1="xp#", str2="xyz##"
    Output: true
    Explanation: After applying backspaces the strings become "x" and "x" respectively.
    In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
"""


def backspace_compare_extra_space(str1, str2):
    # TODO: Write your code here

    str1_copy = ""
    for char in str1:
        if char == "#":
            str1_copy = str1_copy[0:-1]
        else:
            str1_copy += char

    str2_copy = ""
    for char in str2:
        if char == "#":
            str2_copy = str2_copy[0:-1]
        else:
            str2_copy += char

    if len(str1_copy) == len(str2_copy):
        for i in range(len(str1_copy)):
            if str1_copy[i] == str2_copy[i]:
                continue
            else:
                return False
        return True

    return False


print(backspace_compare_extra_space("xy#z", "xzz#"))
print(backspace_compare_extra_space("xy#z", "xyz#"))
print(backspace_compare_extra_space("xp#", "xyz##"))
print(backspace_compare_extra_space("xywrrmp", "xywrrmu#p"))
print(backspace_compare_extra_space("ab#c", "ad#c"))


def backspace_compare(s: str, t: str) -> bool:
    index1 = len(s) - 1
    index2 = len(t) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_non_space_char(s, index1)
        i2 = get_next_non_space_char(t, index2)

        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if s[i1] != t[i2]:
            return False

        index1 = i1 - 1
        index2 = i2 - 1
    return True


def get_next_non_space_char(string, index):
    backspace = 0
    while index >= 0:
        if string[index] == "#":
            backspace += 1
        elif backspace > 0:
            backspace -= 1
        else:
            break

        index -= 1

    return index


print(" ===================== ")
print(backspace_compare("xy#z", "xzz#"))
print(backspace_compare("xy#z", "xyz#"))
print(backspace_compare("xp#", "xyz##"))
print(backspace_compare("xywrrmp", "xywrrmu#p"))
print(backspace_compare("ab#c", "ad#c"))
