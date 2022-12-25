import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


total_sum = -math.inf


class Solution:
    def maxPathSum(self, root) -> int:
        self.maxPathSumRec(root)
        return total_sum

    def maxPathSumRec(self, root):
        global total_sum
        if root is None:
            return 0
        left_subtree_max_sum = max(self.maxPathSumRec(root.left), 0)
        right_subtree_max_sum = max(self.maxPathSumRec(root.right), 0)
        max_through_root = max(
            left_subtree_max_sum + root.val, right_subtree_max_sum + root.val
        )
        total_sum = max(
            total_sum, left_subtree_max_sum + right_subtree_max_sum + root.val
        )
        return max_through_root


root = TreeNode(-1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Maximum Path Sum: " + str(Solution().maxPathSum(root)))
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
print("Maximum Path Sum: " + str(Solution().maxPathSum(root)))
