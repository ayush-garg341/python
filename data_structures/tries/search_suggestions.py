class TrieNode(object):
    def __init__(self):
        self.search_words = []
        self.children = {}


class SearchSuggestions:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        self.insert_char(0, word, self.root)

    def insert_char(self, idx, string, root):
        if idx >= len(string):
            return
        char = string[idx]
        if char not in root.children:
            root.children[char] = TrieNode()
        node = root.children[char]
        if len(node.search_words) < 3:
            node.search_words.append(string)
        self.insert_char(idx + 1, string, root.children[char])

    def search(self, word):
        result = []
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                temp = [[] for _ in range(len(word) - i)]
                return result + temp
            else:
                result.append(node.children[char].search_words)
                node = node.children[char]

        return result


def suggested_products(products, search_word):
    trie = SearchSuggestions()
    products.sort()
    for product in products:
        trie.add(product)
    result = trie.search(search_word)
    return result


print(
    suggested_products(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
)
