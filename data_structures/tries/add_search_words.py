class TrieNode:
    # Initialize TrieNode instance
    def __init__(self):
        self.children = []
        self.is_word = False
        for i in range(0, 26):
            self.children.append(None)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            idx = (ord(char) - 97) % 26
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_word = True

    def search_word(self, word):
        return self.search_word_rec(0, word, self.root)

    def search_word_rec(self, idx, word, node):
        if idx >= len(word):
            return False

        char = word[idx]
        if char == ".":
            for i in range(0, 26):
                if idx == len(word) - 1:
                    if node.children[i] and node.children[i].is_word:
                        return True
                elif node.children[i]:
                    val = self.search_word_rec(idx + 1, word, node.children[i])
                    if val:
                        return True
        else:
            char_idx = (ord(char) - 97) % 26
            if node.children[char_idx] is None:
                return False
            else:
                if idx == len(word) - 1 and node.children[char_idx].is_word:
                    return True
                node = node.children[char_idx]
                return self.search_word_rec(idx + 1, word, node)

        return False


class WordDictionary:
    def __init__(self):
        self.words = []
        self.trie = Trie()

    def add_word(self, word):
        self.words.append(word)
        self.trie.add_word(word)

    def search_word(self, word):
        return self.trie.search_word(word)

    def get_words(self):
        return self.words


wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
print(wd.get_words())
print(wd.search_word("pad"))
print(wd.search_word("bad"))
print(wd.search_word(".ad"))
print(wd.search_word("b.."))

print("======================")
wd = WordDictionary()
wd.add_word("hello")
wd.add_word("help")
wd.add_word("hi")
print(wd.get_words())
print(wd.search_word("h."))


print("======================")
wd = WordDictionary()
wd.add_word("bin")
wd.add_word("data")
print(wd.get_words())
print(wd.search_word(".n"))
print(wd.search_word("d.t."))

print("====================")
wd = WordDictionary()
print(wd.get_words())
wd.add_word("apple")
wd.add_word("grape")
print(wd.get_words())
print(wd.search_word("strawberry"))
wd.add_word("banana")
wd.add_word("banan")
print(wd.search_word("bana.."))
print(wd.search_word("ba...a"))
print(wd.get_words())
