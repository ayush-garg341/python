"""
For a given string, st, find whether or not a permutation of this string
is a palindrome.
You should return TRUE if such a permutation is possible and
FALSE if it isn’t possible.
"""


def permute_palindrome(st):
    st_hash = dict()
    for char in st:
        if char not in st_hash:
            st_hash[char] = 0
        st_hash[char] += 1

    odd_found = False
    for k, v in st_hash.items():
        if v % 2 == 1 and odd_found is not True:
            odd_found = True
        elif v % 2 == 1 and odd_found is True:
            return False
    return True


print(permute_palindrome("aab"))
print(permute_palindrome("abc"))
