"""
    author:- Ayush Garg

    Construct binary tree from pre-order and in-order traversal arrays.
    Input:
        1. Post-order traversal array of a binary tree.
        2. In-order traversal array of a binary tree.
    Output:
        1. Binary tree root node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


post_order = ["d", "e", "b", "f", "g", "c", "a"]
in_order = ["d", "b", "e", "a", "f", "c", "g"]


class BinaryTree:
    def __init__(self, post_order):
        self.root = None
        self.post_order = post_order

    def check_element_pos_inorder(self, in_order, elt):
        for i in range(0, len(in_order)):
            if in_order[i] == elt:
                return i
        return -1

    def construct_tree(self, in_order):
        if len(self.post_order) == 0 or len(in_order) == 0:
            return
        root_elt = self.post_order[-1]
        self.post_order = self.post_order[0 : len(self.post_order) - 1]
        root = Node(root_elt)
        in_order_idx = self.check_element_pos_inorder(in_order, root_elt)
        if in_order_idx != -1:
            in_order_left = in_order[0:in_order_idx]
            in_order_right = in_order[in_order_idx + 1 :]
            if len(in_order_right) != 0:
                root.right = self.construct_tree(in_order_right)
            if len(in_order_left) != 0:
                root.left = self.construct_tree(in_order_left)
        return root


bt = BinaryTree(post_order)

root = bt.construct_tree(in_order)
