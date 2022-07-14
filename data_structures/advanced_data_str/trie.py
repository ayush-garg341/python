"""
Trie data structure implementation useful for strings/prefix search.
"""


class TrieNode:
    def __init__(self):
        self.children_map = dict()
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def traverse(self):
        self.traverse_all_words(self.root)

    def traverse_all_words(self, current_node):
        for child, node in current_node.children_map.items():
            print(child, end=" - ")
            self.traverse_all_words(node)

    def insert_iter(self, word):
        current = self.root
        for char in word:
            if char in current.children_map:
                new_node = current.children_map[char]
            else:
                new_node = TrieNode()
                current.children_map[char] = new_node
            current = new_node

        current.end_of_word = True

    def insert_rec(self, word):
        self.insert(word, 0, self.root)

    def insert(self, word, index, current_node):
        if index == len(word):
            current_node.end_of_word = True
            return
        else:
            char = word[index]
            if char in current_node.children_map:
                new_node = current_node.children_map[char]
            else:
                new_node = TrieNode()
                current_node.children_map[char] = new_node
            self.insert(word, index + 1, new_node)

    def search(self, prefix, word=False):
        if word:
            return self.search_word(self.root, prefix, 0)
        else:
            return self.search_prefix(self.root, prefix, 0)

    def search_word(self, current_node, word, index):
        if len(word) == index:
            return current_node.end_of_word
        else:
            char = word[index]
            if char in current_node.children_map:
                new_node = current_node.children_map[char]
                return self.search_word(new_node, word, index + 1)
            else:
                return False

    def search_prefix(self, current_node, prefix, index):
        if len(prefix) == index:
            return True
        else:
            char = prefix[index]
            if char in current_node.children_map:
                new_node = current_node.children_map[char]
                return self.search_prefix(new_node, prefix, index + 1)
            else:
                return False

    def delete(self, word):
        return self.delete_rec(self.root, word, 0)

    def delete_rec(self, current_node, word, index):
        if len(word) == index:
            if not current_node.end_of_word:
                return False
            # handles the case when we have two complete words abc, abcd and we want to delete abc
            # we can not delete abc since there is another word abcd present.
            # We can mark abc end of word as False ( soft delete )
            # We will delete only if current_node does not have any children.
            current_node.end_of_word = False
            return len(current_node.children_map) == 0
        char = word[index]
        if char not in current_node.children_map:
            return False
        node = current_node.children_map[char]
        delete = self.delete_rec(node, word, index + 1)
        if delete:
            del current_node.children_map[char]
            return len(current_node.children_map) == 0

        return False


trie = Trie()
trie.insert_iter("abcd")
trie.insert_rec("abc")
trie.traverse()
print()
print(trie.search("ab", True))
print(trie.search("abc", True))
print(trie.search("abcd", True))
print(trie.search("abcde", True))

print()

print(trie.search("ab"))
print(trie.search("abc"))
print(trie.search("a"))

print("Deleteing word abc")
print(trie.delete("abc"))
print("Searching for word abc")
print(trie.search("abc", True))
print("searching for prefix abc")
print(trie.search("abc"))
print("Searching for word abcd")
print(trie.search("abcd", True))
