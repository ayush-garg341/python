"""
Given a binary tree, return all root-to-leaf paths.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root):
    allPaths = []
    find_all_paths(root, [], allPaths)
    return allPaths


def find_all_paths(root, current_path, allPaths):
    if root is not None:
        current_path.append(root.val)
        find_all_paths(root.left, current_path, allPaths)
        find_all_paths(root.right, current_path, allPaths)
        if not root.left and not root.right:
            allPaths.append(list(current_path))

        current_path.pop()


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths from root to leaf " + str(sum) + ": " + str(find_paths(root)))


main()
