"""
Given a list of words or phrases, group the words that are anagrams
of each other.
An anagram is a word or phrase formed from another word by rearranging
its letters.
"""


def group_anagrams_naive(strs: list[str]) -> list[list[str]]:
    track = dict()
    for string in strs:
        sorted_string = "".join(sorted(string))
        if sorted_string in track:
            track[sorted_string].append(string)
        else:
            track[sorted_string] = [string]

    result = []
    for key, value in track.items():
        result.append(value)

    return result


print(
    group_anagrams_naive(
        ["state", "save", "robed", "sat", "taste", "bored", "vase", "bore"]
    )
)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    track = dict()
    for string in strs:
        freq_index = [0] * 26
        for char in string:
            idx = ord(char) - ord("a")
            freq_index[idx] += 1

        tup = tuple(freq_index)
        if tup in track:
            track[tup].append(string)
        else:
            track[tup] = [string]

    results = []
    for k, v in track.items():
        results.append(v)

    return results


print(
    group_anagrams(["state", "save", "robed", "sat", "taste", "bored", "vase", "bore"])
)
