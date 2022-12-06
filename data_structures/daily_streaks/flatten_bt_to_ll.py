"""
Given the root of a binary tree, flatten the tree into a "linked list":
1. The "linked list" should use the same TreeNode class where the right child
    pointer points to the next node in the list and the left child pointer is always null.
2. The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenRecursive(root)

    def flattenRecursive(self, root):
        if root is None:
            return
        temp = root.right
        if self.prev is None:
            self.prev = root
        else:
            self.prev.right = root
            self.prev = root
        self.flattenRecursive(root.left)
        root.left = None
        self.flattenRecursive(temp)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
