"""
Find the path with the maximum sum in a given binary tree.
A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
"""


import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


total_sum = -math.inf


def find_maximum_path_sum(root):
    # TODO: Write your code here
    find_maximum_path_sum_rec(root)
    return total_sum


def find_maximum_path_sum_rec(current_node):
    global total_sum
    if current_node is None:
        return 0
    left_tree_sum = find_maximum_path_sum_rec(current_node.left)
    right_tree_sum = find_maximum_path_sum_rec(current_node.right)

    left_tree_sum = max(left_tree_sum, 0)
    right_tree_sum = max(right_tree_sum, 0)
    s = left_tree_sum + right_tree_sum + current_node.val
    total_sum = max(total_sum, s)

    return max(left_tree_sum, right_tree_sum) + current_node.val


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    # root = TreeNode(-3)
    # root.left = TreeNode(-1)
    # print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
