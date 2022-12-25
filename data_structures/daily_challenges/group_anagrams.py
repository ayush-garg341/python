"""
Write a function that takes in an array of string and groups anagrams together.

Anagrams are string made up of exactly the same letters, where order does not matter.
ex. cinema and iceman
    foo and ofo
"""


def groupAnagrams(words):
    """
    HINT:- We know that alphabetical ordering of all anagrams will be same.
    Time complexitty :- O(w*n*log n) -> w - number of words, nlogn -> sorting time.
    Space complexitty :- O(wn), n -> length of longest word.
    """
    result = []
    word_map = {}
    for i in range(len(words)):
        word = words[i]
        alphabetical_order = "".join(sorted(word))
        if alphabetical_order not in word_map:
            word_map[alphabetical_order] = []
        word_map[alphabetical_order].append(i)

    for word, indexes in word_map.items():
        anagrams = []
        for index in indexes:
            anagrams.append(words[index])
        result.append(anagrams)
    return result


print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))


from collections import Counter


def groupAnagramsUsingFrozenSet(words):
    anagrams = {}
    for word in words:
        hash_key = frozenset(Counter(word).items())
        if hash_key not in anagrams:
            anagrams[hash_key] = []
        anagrams[hash_key].append(word)
    return list(anagrams.values())


print(
    groupAnagramsUsingFrozenSet(
        ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    )
)


"""
The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation.
Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.
But like sets, it is not ordered (the elements can be set at any index).
"""
