"""
Two strings are isomorphic if a fixed mapping exists from the characters
of one string to the characters of the other string.

Two different characters cannot map to the same character.
"""


def is_isomorphic(string1, string2):
    mapping = dict()
    already_mapped = set()
    l1 = len(string1)
    l2 = len(string2)
    if l1 != l2:
        return False
    for i in range(l1):
        c2 = string2[i]
        c1 = string1[i]
        if c1 not in mapping:
            if c2 not in already_mapped:
                already_mapped.add(c2)
                mapping[c1] = c2
            else:
                return False
        else:
            existing = mapping[c1]
            if c2 != existing:
                return False

    return True


print(is_isomorphic("ACAB", "XCXY"))
print(is_isomorphic("aab", "xyz"))
print(is_isomorphic("awz", "xwz"))
