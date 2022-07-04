# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    elts = []
    find_kth_largest_value_rec(tree, elts, k)
    return elts[-k]


def find_kth_largest_value_rec(root, elts, k):
    if root is None:
        return
    find_kth_largest_value_rec(root.left, elts, k)
    elts.append(root.value)
    find_kth_largest_value_rec(root.right, elts, k)


# Solution two much optimized in terms of space and time complexity
class TreeInfo:
    def __init__(self, number_of_nodes_visited, latest_visited_node):
        self.number_of_nodes_visited = number_of_nodes_visited
        self.latest_visited_node = latest_visited_node


def findKthLargestValueInBst(tree, k):
    tree_info = TreeInfo(0, -1)
    reverse_inorder_traversal(tree, tree_info, k)
    return tree_info.latest_visited_node


def reverse_inorder_traversal(root, tree_info, k):
    if root is None or tree_info.number_of_nodes_visited == k:
        return

    reverse_inorder_traversal(root.right, tree_info, k)
    if tree_info.number_of_nodes_visited < k:
        tree_info.number_of_nodes_visited += 1
        tree_info.latest_visited_node = root.value
        reverse_inorder_traversal(root.left, tree_info, k)
