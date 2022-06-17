def longest_palin_substr(string) -> str:
    """
    This solution will give TLE error
    """
    n = len(string)
    dp = [[0 for i in range(n)] for j in range(n)]

    max_len = -1

    end = -1
    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            if string[i] == string[j]:
                remaining_len = j - i - 1
                if remaining_len == dp[i + 1][j - 1]:
                    dp[i][j] = 2 + remaining_len
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end = j

    if end == -1:
        return string[0]
    return string[end - max_len + 1 : end + 1]


print(longest_palin_substr("cbbd"))
print(longest_palin_substr("babad"))
print(longest_palin_substr("cddpd"))
print(longest_palin_substr("pqr"))
print(longest_palin_substr("aaaa"))
print(longest_palin_substr("abcdcb"))
print(longest_palin_substr("babaddtattarrattatddetartrateedredividerb"))


def longest_palin_substr_without_tle(string) -> str:
    n = len(string)
    dp = [[False for i in range(n)] for j in range(n)]

    char = string[0]
    for i in range(n):
        dp[i][i] = True

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if string[i] != string[j]:
                continue
            if (j - i == 1) or dp[i + 1][j - 1]:
                dp[i][j] = True
                if len(char) < j - i + 1:
                    char = string[i : j + 1]

    return char


print(" ====================== ")

print(longest_palin_substr_without_tle("cbbd"))
print(longest_palin_substr_without_tle("babad"))
print(longest_palin_substr_without_tle("cddpd"))
print(longest_palin_substr_without_tle("pqr"))
print(longest_palin_substr_without_tle("aaaa"))
print(longest_palin_substr_without_tle("abcdcb"))
print(longest_palin_substr_without_tle("babaddtattarrattatddetartrateedredividerb"))
