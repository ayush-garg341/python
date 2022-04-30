"""
Given a binary tree, find the root-to-leaf path with the maximum sum.
"""

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root):
    allPaths = []
    current_sum = 0
    find_path_recursive(root, current_sum, [], allPaths)
    return allPaths[-1]


s = -math.inf


def find_path_recursive(root, current_sum, current_path, allPaths):
    global s
    if root is not None:
        current_path.append(root.val)
        current_sum += root.val
        find_path_recursive(root.left, current_sum, current_path, allPaths)
        find_path_recursive(root.right, current_sum, current_path, allPaths)
        if not root.left and not root.right:
            if current_sum > s:
                s = current_sum
                allPaths.append(list(current_path))
        current_sum -= root.val
        current_path.pop()
        print(s)


s = -math.inf


def find_max_sum(root, current_sum):
    global s
    if root is not None:
        current_sum += root.val
        find_max_sum(root.left, current_sum)
        find_max_sum(root.right, current_sum)
        if not root.left and not root.right:
            if current_sum > s:
                s = current_sum
        current_sum -= root.val


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree path with  max sum " + ": " + str(find_paths(root)))
    find_max_sum(root, 0)
    print("Tree with  max sum " + ": " + str(s))


main()
