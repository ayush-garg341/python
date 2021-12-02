"""
    author:- Ayush Garg

    Construct binary tree from pre-order and in-order traversal arrays.
    Input:
        1. Pre-order traversal array of a binary tree.
        2. In-order traversal array of a binary tree.
    Output:
        1. Binary tree root node.
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

pre_order = [3, 9, 20, 15, 7]
in_order = [9, 3, 15, 20, 7]


class BinaryTree:

    def __init__(self, pre_order):
        self.root = None
        self.pre_order = pre_order

    def check_element_pos_inorder(self, in_order, elt):
        for i in range(0, len(in_order)):
            if in_order[i] == elt:
                return i
        return -1

    def construct_tree(self,in_order):
        if len(self.pre_order) == 0 or len(in_order)==0:
            return
        root_elt = self.pre_order[0]
        self.pre_order = self.pre_order[1:]
        root = Node(root_elt)
        in_order_idx = self.check_element_pos_inorder(in_order, root_elt)
        if in_order_idx!=-1:
            in_order_left = in_order[0:in_order_idx]
            in_order_right = in_order[in_order_idx+1:]
            if len(in_order_left)!=0:
                root.left = self.construct_tree(in_order_left)
            if len(in_order_right)!=0:
                root.right = self.construct_tree(in_order_right)
        return root

bt = BinaryTree(pre_order)

root = bt.construct_tree(in_order)
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.right.left.data)
print(root.right.right.data)
