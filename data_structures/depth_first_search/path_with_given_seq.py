"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    exist = False
    exist = find_path_seq_recursive(root, sequence, 0)
    if exist:
        return True
    return False


def find_path_seq_recursive(root, seq, index):
    if root is None or index >= len(seq):
        return False
    if root.left is None and root.right is None:
        if root.val == seq[index] and index == len(seq) - 1:
            return True
        return False
    if root.val == seq[index]:
        p1 = find_path_seq_recursive(root.left, seq, index + 1)
        p2 = find_path_seq_recursive(root.right, seq, index + 1)
        return p1 or p2

    return False


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
    print("Tree has path sequence: " + str(find_path(root, [1, 2, 1])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 5])))


main()
