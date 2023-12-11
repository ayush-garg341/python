"""
Construct a height balanced BST from sorted array.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sorted_array_to_bst(nums):
    # Replace this placeholder return statement with your code
    root = sorted_array_to_bst_rec(nums, 0, len(nums) - 1)
    return root


def sorted_array_to_bst_rec(nums, start, end):
    if end - start <= 0:
        return None

    mid = (start + end) // 2
    val = nums[mid]
    root = TreeNode(val)

    root.left = sorted_array_to_bst_rec(nums, start, mid - 1)
    root.right = sorted_array_to_bst_rec(nums, mid + 1, end)

    return root


root = sorted_array_to_bst([11, 22, 33, 44, 55, 66, 77, 88])
print(root.data)
