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


def check_same_bst_or_not(array1, array2):
    """
    Arrays can have duplicates too
    """
    n1 = len(array1)
    n2 = len(array2)

    if n1 != n2:
        return False

    if array1[0] != array2[0]:
        return False

    return check_same_bst_or_not_rec(array1, array2)

def check_same_bst_or_not_rec(arr1, arr2):

    if len(arr1) != len(arr2):
        return False

    if len(arr1) == 0 or len(arr2) == 0:
        return True

    if arr1[0] != arr2[0]:
        return False

    left_tree_arr_1 = [num for num in arr1[1:] if num < arr1[0]]
    left_tree_arr_2 = [num for num in arr2[1:] if num < arr2[0]]

    right_tree_arr_1 = [num for num in arr1[1:] if num >= arr1[0]]
    right_tree_arr_2 = [num for num in arr2[1:] if num >= arr2[0]]

    return check_same_bst_or_not_rec(left_tree_arr_1, left_tree_arr_2) and check_same_bst_or_not_rec(right_tree_arr_1, right_tree_arr_2)















