"""
Print right view of binary tree
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def right_view(self, root):
        data = []
        if root is None:
            return data
        self.right_view_rec(root, data, 1)
        return data

    def right_view_rec(self, root, data, level):
        if root is None:
            return

        if len(data) < level:
            data.append(root.val)
        level += 1
        self.right_view_rec(root.right, data, level)
        self.right_view_rec(root.left, data, level)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)

soln = Solution()
print(soln.right_view(root))
