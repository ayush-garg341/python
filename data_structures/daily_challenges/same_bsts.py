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
    return check_valid_bst_recursive(
        root.left, left_val, root.val
    ) and check_valid_bst_recursive(root.right, root.val, right_val)


def check_same_bst_or_not(array1, array2):
    """
    Arrays can have duplicates too
    """
    n1 = len(array1)
    n2 = len(array2)

    if n1 != n2:
        return False

    return check_same_bst_or_not_rec_space_eff(
        array1, array2, 0, 0, -math.inf, math.inf
    )


def check_same_bst_or_not_rec_space_eff(arr1, arr2, idx1, idx2, left_val, right_val):

    # if (idx1 == len(arr1) and idx2 != len(arr2)) or (idx1 != len(arr1) and idx2 == len(arr2)):
    # return False

    if idx1 == len(arr1) and idx2 == len(arr2):
        return True

    if arr1[idx1] != arr2[idx2]:
        return False

    root_val = arr1[idx1]

    left_idx1 = len(arr1)
    left_idx2 = len(arr2)

    for i in range(idx1 + 1, len(arr1)):
        if arr1[i] < root_val and arr1[i] >= left_val:
            left_idx1 = i
            break
    for i in range(idx2 + 1, len(arr2)):
        if arr2[i] < root_val and arr2[i] >= left_val:
            left_idx2 = i
            break

    right_idx1 = len(arr1)
    right_idx2 = len(arr2)

    for i in range(idx1 + 1, len(arr1)):
        if arr1[i] >= root_val and arr1[i] < right_val:
            right_idx1 = i
            break
    for i in range(idx2 + 1, len(arr2)):
        if arr2[i] >= root_val and arr2[i] < right_val:
            right_idx2 = i
            break

    return check_same_bst_or_not_rec_space_eff(
        arr1, arr2, left_idx1, left_idx2, left_val, root_val
    ) and check_same_bst_or_not_rec_space_eff(
        arr1, arr2, right_idx1, right_idx2, root_val, right_val
    )


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

    return check_same_bst_or_not_rec(
        left_tree_arr_1, left_tree_arr_2
    ) and check_same_bst_or_not_rec(right_tree_arr_1, right_tree_arr_2)


def construct_bst_and_check(arrayOne, arrayTwo):
    # TODO
    if len(arrayOne) != len(arrayTwo):
        return False
    tree_a_dict = {}
    tree_b_dict = {}

    for i in range(len(arrayOne)):
        flag = True
        idx = 0
        while flag:
            if idx in tree_a_dict:
                if arrayOne[i] >= tree_a_dict[idx]:
                    idx = 2 * idx + 2
                else:
                    idx = 2 * idx + 1
            else:
                tree_a_dict[idx] = arrayOne[i]
                flag = False

    for i in range(len(arrayTwo)):
        flag = True
        idx = 0
        while flag:
            if idx in tree_b_dict:
                if arrayTwo[i] >= tree_b_dict[idx]:
                    idx = 2 * idx + 2
                else:
                    idx = 2 * idx + 1
            else:
                tree_b_dict[idx] = arrayTwo[i]
                if idx in tree_a_dict:
                    if tree_a_dict[idx] != tree_b_dict[idx]:
                        return False
                else:
                    return False
                flag = False

    return True


arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

print(check_same_bst_or_not(arrayOne, arrayTwo))

print(construct_bst_and_check(arrayOne, arrayTwo))
