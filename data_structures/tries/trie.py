"""
Implement trie
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        # Write your code here
        self.root = TrieNode()

    # inserting string in trie
    def insert(self, string):
        # Write your code here
        self.insert_char(0, string, self.root)

    def insert_char(self, idx, string, root):
        if idx >= len(string):
            return
        char = string[idx]
        if char not in root.children:
            root.children[char] = TrieNode()
        if idx == len(string) - 1:
            root.children[char].is_word = True
        else:
            self.insert_char(idx + 1, string, root.children[char])

    # searching for a string
    def search(self, string):
        # Replace this placeholder return statement with your code
        return self.search_rec(0, string, self.root)

    # searching for a prefix
    def search_prefix(self, prefix):
        # Replace this placeholder return statement with your code
        return self.search_prefix_rec(0, prefix, self.root)

    def search_prefix_rec(self, idx, prefix, root):
        if idx >= len(prefix):
            return True
        char = prefix[idx]
        if char in root.children:
            return self.search_prefix_rec(idx + 1, prefix, root.children[char])
        return False

    def search_rec(self, idx, string, root):
        if idx >= len(string):
            return False
        char = string[idx]
        if char in root.children:
            if idx == len(string) - 1 and root.children[char].is_word:
                return True
            return self.search_rec(idx + 1, string, root.children[char])
        return False

    def search_shortest_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char in node.children:
                prefix += char
                if node.children[char].is_word is True:
                    return prefix
                node = node.children[char]
            else:
                return None


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.search_prefix("app"))
trie.insert("app")
print(trie.search("app"))
