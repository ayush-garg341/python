from trie import Trie


def replace_words(sentence, dictionary):
    # Replace this placeholder return statement with your code
    node = Trie()
    for prefix in dictionary:
        node.insert(prefix)

    short_string = []
    words = sentence.split(" ")
    for word in words:
        prefix = node.search_shortest_prefix(word)
        if prefix:
            short_string.append(prefix)
        else:
            short_string.append(word)

    return " ".join(short_string)


print(
    replace_words(
        "the quick brown fox jumps over the lazy dog", ["qui", "f", "la", "d"]
    )
)
