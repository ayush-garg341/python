"""
Flatten binary tree to pre-order traversal list
"""


class Solution:
    prev = None

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_rec(root)

    def flatten_rec(self, root):
        if root is None:
            return
        temp = root.right
        if self.prev is None:
            self.prev = root
        else:
            self.prev.right = root
            self.prev = root
        self.flatten_rec(root.left)
        root.left = None
        self.flatten_rec(temp)
