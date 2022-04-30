"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each
path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    current_sum = 0
    find_path_recursive(root, sum, current_sum, [], allPaths)
    return allPaths


def find_path_recursive(root, sum, current_sum, current_path, allPaths):
    """
    List are passed by reference and hence values keep changing in them.
    """
    if root is not None:
        current_path.append(root.val)
        current_sum += root.val
        find_path_recursive(root.left, sum, current_sum, current_path, allPaths)
        find_path_recursive(root.right, sum, current_sum, current_path, allPaths)
        if not root.left and not root.right:
            if current_sum == sum:
                """
                If we dont use list on current_path, finally it will be empty and hence current_path will be empty
                in allPaths. So need to copy this using list.
                """
                allPaths.append(list(current_path))
        current_sum -= root.val
        current_path.pop()


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


main()
