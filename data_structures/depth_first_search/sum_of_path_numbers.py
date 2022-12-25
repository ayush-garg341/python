"""
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers_leaf_to_root(root):
    current_path = []
    allPaths = []
    find_sum_of_path_numbers_leaf_to_root_recursive(root, current_path, allPaths)
    print(allPaths)
    total_sum = 0
    for path in allPaths:
        current_sum = 0
        power = 1
        for i in range(len(path) - 1, -1, -1):
            current_sum += path[i] * power
            power = power * 10
        total_sum += current_sum

    return total_sum


def find_sum_of_path_numbers_leaf_to_root_recursive(root, current_path, allPaths):
    if root is not None:
        current_path.append(root.val)
        find_sum_of_path_numbers_leaf_to_root_recursive(
            root.left, current_path, allPaths
        )
        find_sum_of_path_numbers_leaf_to_root_recursive(
            root.right, current_path, allPaths
        )
        if not root.left and not root.right:
            allPaths.append(list(current_path))
        current_path.pop()


def find_sum_of_path_numbers_root_to_leaf(root):
    total_sum = find_sum_of_path_numbers_root_to_leaf_recursive(root, 0)
    return total_sum


def find_sum_of_path_numbers_root_to_leaf_recursive(root, path_sum):
    if root is None:
        return 0
    path_sum = path_sum * 10 + root.val
    if root.left is None and root.right is None:
        return path_sum

    s1 = find_sum_of_path_numbers_root_to_leaf_recursive(root.left, path_sum)
    s2 = find_sum_of_path_numbers_root_to_leaf_recursive(root.right, path_sum)

    return s1 + s2


s = 0


def find_sum_of_path_numbers(root):
    find_sum_of_path_numbers_recursive(root, 0, 1)
    return s


def find_sum_of_path_numbers_recursive(root, current_sum, power):
    """
    Calculating all path sum if root is at 0th place, root.left and root.right is at 1th place and so on....
    """
    global s
    if root is not None:
        current_sum += root.val * power
        find_sum_of_path_numbers_recursive(root.left, current_sum, power * 10)
        find_sum_of_path_numbers_recursive(root.right, current_sum, power * 10)
        if not root.left and not root.right:
            print(current_sum)
            s += current_sum
        current_sum -= root.val * power
        power = power // 10


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print(
        "Total Sum of Path Numbers: " + str(find_sum_of_path_numbers_leaf_to_root(root))
    )
    print(
        "Total Sum of Path Numbers: " + str(find_sum_of_path_numbers_root_to_leaf(root))
    )


main()
