"""
Invert binary tree i.e mirror binary tree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.mirror_binary_tree_rec(root)
        return root

    def mirror_binary_tree_rec(self, root):
        if root is None:
            return

        self.mirror_binary_tree_rec(root.left)
        self.mirror_binary_tree_rec(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
