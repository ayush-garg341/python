"""
Find lowest common ancestor of two nodes p and q.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        root = self.lowestCommonAncestorRec(root, p, q)
        return root

    def lowestCommonAncestorRec(self, root, p, q):
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestorRec(root.left, p, q)
        right = self.lowestCommonAncestorRec(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right
