"""
Write a function that takes in binary tree and return its max path sum.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes.
A path sum is the sum of the values of the nodes in a particular path.
"""

import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = Node(1)
tree.left = Node(2)
tree.left.left = Node(4)
tree.left.right = Node(5)

tree.right = Node(3)
tree.right.left = Node(6)
tree.right.right = Node(7)


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


print("Inorder traversal")
inorder_traversal(tree)
print()


class Sum:
    max_sum = -math.inf


def max_path_sum_through_root(root):
    max_path_sum(root.left, 0)
    left_subtree_max_path_sum = Sum.max_sum
    print("left subtree max path sum = ", left_subtree_max_path_sum)
    Sum.max_sum = -math.inf
    max_path_sum(root, 0)
    right_subtree_max_path_sum = Sum.max_sum
    print("right_subtree_max_path_sum = ", right_subtree_max_path_sum)

    return left_subtree_max_path_sum + right_subtree_max_path_sum


def max_path_sum(root, s):
    if root is None:
        return 0
    s += root.val
    if root.left is None and root.right is None:
        temp_sum = Sum.max_sum
        max_sum = max(temp_sum, s)
        Sum.max_sum = max_sum

    else:
        max_path_sum(root.left, s)
        max_path_sum(root.right, s)


# print("max path sum between two connected nodes through root")
# print(max_path_sum_through_root(tree))


def max_path_sum_between_two_nodes(root):

    if root is None:
        return 0

    left_subtree = max_path_sum_between_two_nodes(root.left)
    right_subtree = max_path_sum_between_two_nodes(root.right)

    max_val = max(root.val, max(left_subtree + root.val, right_subtree + root.val))

    max_sum = max(max_val, left_subtree + right_subtree + root.val)

    temp_sum = Sum.max_sum
    temp_max = max(temp_sum, max(max_val, max_sum))
    Sum.max_sum = temp_max

    return max_val


print("max path sum between two connected nodes")
max_path_sum_between_two_nodes(tree)

print(Sum.max_sum)
