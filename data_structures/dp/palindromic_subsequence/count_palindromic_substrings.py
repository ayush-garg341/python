"""
Given a string, find the total number of palindromic substrings in it.
Please note we need to find the total number of substr and not subseq.

example1:
    Input: "abdbca"
    Output: 7
    Explanation: Here are the palindromic substrings, "a", "b", "d",
                                                "b", "c", "a", "bdb".

example2:
    Input: = "cddpd"
    Output: 7
    Explanation: Here are the palindromic substrings, "c", "d", "d",
                                                "p", "d", "dd", "dpd".

example3:
    Input: = "pqr"
    Output: 3
    Explanation: Here are the palindromic substrings,"p", "q", "r".
"""


# def count_palin_substr(string):
# start = 0
# end = len(string) - 1
# count = count_palin_substr_recursive(string, start, end)
# return count


# def count_palin_substr_recursive(string: str, start: int, end: int) -> int:
# print("start, end = ", start, end)

# if start == end:
# return 1

# if start > end:
# return 0

# count1, count2 = 0, 0
# if string[start] == string[end]:
# remaining_len = end - start - 1
# if remaining_len == count_palin_substr_recursive(string, start + 1, end - 1):
# return 3 + remaining_len
# count1 = 1 + count_palin_substr_recursive(string, start + 1, end)
# count2 = 1 + count_palin_substr_recursive(string, start, end - 1)
# return max(count1, count2)


# print("========== count palindromic substring brute force recusrive ========")
# print(count_palin_substr("abdbca"))
# print(count_palin_substr("cddpd"))
# print(count_palin_substr("pqr"))


def count_palin_substr_dp_bottom_up_tabular(string):
    n = len(string)
    if n == 0:
        return -1
    dp = [[False for i in range(n)] for j in range(n)]

    count = 0
    for i in range(n):
        dp[i][i] = True
        count += 1

    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    count += 1

    return count


print("========== count palindromic substr dp bottom up tabular ========")
print(count_palin_substr_dp_bottom_up_tabular("abdbca"))
print(count_palin_substr_dp_bottom_up_tabular("cddpd"))
print(count_palin_substr_dp_bottom_up_tabular("pqr"))
