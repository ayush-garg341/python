"""
Given two input arrays, check if they represent the same bsts.
BST property => The value at a given node is strictly greater than the value of every node to its left and it's value is less than or equal to values of nodes to its right.

example1:
    input:
        array1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        array2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    output:
        True
"""

import math

def check_valid_bst(root):
    return check_valid_bst_recursive(root, -math.inf, math.inf)


def check_valid_bst_recursive(root, left_val, right_val):
    if not root:
        return True
    if root.val >= right_val or root.val <= left_val:
        return False
    return check_valid_bst_recursive(root.left, left_val, root.val) and check_valid_bst_recursive(root.right, root.val, right_val)
