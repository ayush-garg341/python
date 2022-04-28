"""
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set
of nodes visible when the tree is seen from the right side.
"""

from __future__ import print_function


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result
    deq = []
    deq.append(root)
    while len(deq):
        size = len(deq)
        while size != 0:
            pop = deq.pop(0)
            if size == 1:
                result.append(pop)
            size -= 1
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)
    return result


def tree_left_view(root):
    result = []
    if root is None:
        return result
    deq = []
    deq.append(root)
    while len(deq):
        size = len(deq)
        index = size
        while size != 0:
            pop = deq.pop(0)
            if size == index:
                result.append(pop)
            size -= 1
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end="")

    result = tree_left_view(root)
    print()
    print("Tree left view: ")
    for node in result:
        print(str(node.val) + " ", end="")
    print()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end="")

    result = tree_left_view(root)
    print()
    print("Tree left view: ")
    for node in result:
        print(str(node.val) + " ", end="")
    print()


main()
