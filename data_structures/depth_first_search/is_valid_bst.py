"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

example1:
    Input: root = [2,1,3]
    Output: true

example2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import Optional

import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    inorder = []
    inorder_traversal(root, inorder)
    for i in range(1, len(inorder)):
        if inorder[i] <= inorder[i - 1]:
            return False

    return True


def inorder_traversal(root, inorder):
    if root is None:
        return

    inorder_traversal(root.left, inorder)
    inorder.append(root.val)
    inorder_traversal(root.right, inorder)


def is_valid_bst_recrusive(root):
    def validate(root, min_val, max_val):
        if root is None:
            return True
        if not (min_val < root.val < max_val):
            return False

        return validate(root.left, min_val, root.val) and validate(root.right, root.val, max_val)

    validate(root, -math.inf, math.inf)
