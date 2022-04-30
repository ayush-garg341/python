"""
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the
node values of that path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    # TODO: Write your code here
    current_sum = 0
    path_exist = has_path_sum(root, sum, current_sum)
    if path_exist:
        return True
    return False


def has_path_sum(root, sum, current_sum):
    if root is None:
        return None

    current_sum += root.val
    s1 = has_path_sum(root.left, sum, current_sum)
    s2 = has_path_sum(root.right, sum, current_sum)
    if s1 or s2:
        return True
    if not root.left and not root.right:
        if current_sum == sum:
            return True
    current_sum -= root.val


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(19)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
