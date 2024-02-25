class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def order(self):
        lexi_order = []
        self.order_rec(self.root, lexi_order, "")
        return lexi_order

    def order_rec(self, node, lexi_order, string):
        for char in node.children:
            if node.children[char].is_word:
                lexi_order.append(int(string + char))
            self.order_rec(node.children[char], lexi_order, string + char)


def lexicographical_order(n):
    trie = Trie()
    for i in range(1, n + 1):
        trie.add_word(str(i))
    return trie.order()


print(lexicographical_order(12))
print(lexicographical_order(22))
print(lexicographical_order(5))
