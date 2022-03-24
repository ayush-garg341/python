"""
Given three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’.
‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’
and the order of letters is preserved too.

example1:
    Input: m="abd", n="cef", p="abcdef"
    Output: true
    Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

example2:
    Input: m="abd", n="cef", p="adcbef"
    Output: false
    Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order.

Approach:
    We can check individual string m and n for the longest subseq in p.
    lca(m, p) -> length of m
    lca(n, p) -> length of n
"""


def brute_force_interleaving_strings(str1, str2, str3):
    m, n, p = len(str1), len(str2), len(str3)
    m_p_len = brute_force_interleaving_strings_recursive(str1, str3, 0, 0)
    n_p_len = brute_force_interleaving_strings_recursive(str2, str3, 0, 0)
    if m_p_len == m and n_p_len == n and m_p_len + n_p_len == p:
        return True
    return False


def brute_force_interleaving_strings_recursive(m: str, p: str, i: int, j: int) -> int:
    if i == len(m) or j == len(p):
        return 0

    if m[i] == p[j]:
        return 1 + brute_force_interleaving_strings_recursive(m, p, i + 1, j + 1)

    c1 = brute_force_interleaving_strings_recursive(m, p, i + 1, j)
    c2 = brute_force_interleaving_strings_recursive(m, p, i, j + 1)

    return max(c1, c2)


print("===== burte force interleaving strings =======")
print(brute_force_interleaving_strings("abd", "cef", "abcdef"))
print(brute_force_interleaving_strings("abd", "cef", "adcbef"))
print(brute_force_interleaving_strings("abcdef", "mnop", "mnaobcdepf"))


def interleaving_strings_brute_force(m, n, p):
    return interleaving_strings_brute_force_recursive(m, n, p, 0, 0, 0)


def interleaving_strings_brute_force_recursive(m, n, p, mIndex, nIndex, pIndex):
    mLen, nLen, pLen = len(m), len(n), len(p)
    if mIndex == mLen and nIndex == nLen and pIndex == pLen:
        return True

    if pIndex == pLen:
        return False

    b1, b2 = False, False

    if mIndex < mLen and m[mIndex] == p[pIndex]:
        b1 = interleaving_strings_brute_force_recursive(m, n, p, mIndex + 1, nIndex, pIndex + 1)
    if nIndex < nLen and n[nIndex] == p[pIndex]:
        b2 = interleaving_strings_brute_force_recursive(m, n, p, mIndex, nIndex + 1, pIndex + 1)

    return b1 or b2


print("===== interleaving strings brut force =======")
print(interleaving_strings_brute_force("abd", "cef", "abcdef"))
print(interleaving_strings_brute_force("abd", "cef", "adcbef"))
print(interleaving_strings_brute_force("abcdef", "mnop", "mnaobcdepf"))
