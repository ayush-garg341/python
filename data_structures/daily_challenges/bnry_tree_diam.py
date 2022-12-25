"""
Take a root of binary tree and return the diameter.
Diameter -> length of longest path between two leaf nodes.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return binaryTreeDiameterRec(tree).diameter


def binaryTreeDiameterRec(root):
    if root is None:
        return TreeInfo(0, 0)

    left_subtree = binaryTreeDiameterRec(root.left)
    right_subtree = binaryTreeDiameterRec(root.right)
    longest_path_so_far = left_subtree.height + right_subtree.height
    max_diameter = max(left_subtree.diameter, right_subtree.diameter)
    current_diameter = max(max_diameter, longest_path_so_far)

    return TreeInfo(
        current_diameter, 1 + max(left_subtree.height, right_subtree.height)
    )


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


root = BinaryTree(1)
root.right = BinaryTree(2)
root.left = BinaryTree(3)

root.left.left = BinaryTree(7)
root.left.right = BinaryTree(4)

root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)

root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)

print(binaryTreeDiameter(root))
