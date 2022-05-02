"""
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
Please note that the paths can start or end at any node but all paths must follow direction from parent to child.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    """Treat each node of a tree as a root node and pass it to calculate the sum."""

    if root is None:
        return 0
    total_paths = 0
    deq = []
    deq.append(root)
    while len(deq):
        size = len(deq)
        while size != 0:
            pop = deq.pop()
            size -= 1
            total_paths += count_paths_with_give_sum(pop, S, 0)
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)

    return total_paths


def count_paths_with_give_sum(root, given_sum, total_sum):
    if root is None:
        return 0

    total_sum = total_sum + root.val

    if root.left is None and root.right is None:
        if total_sum == given_sum:
            return 1
        return 0

    if total_sum == given_sum:
        return (
            1
            + count_paths_with_give_sum(root.left, given_sum, total_sum)
            + count_paths_with_give_sum(root.right, given_sum, total_sum)
        )

    s1 = count_paths_with_give_sum(root.left, given_sum, total_sum)
    s2 = count_paths_with_give_sum(root.right, given_sum, total_sum)

    return s1 + s2


def count_paths_no_extra_traversal(root, S):
    path_count = 0
    path_count = count_paths_no_extra_traversal_rec(root, S, [])
    return path_count


def count_paths_no_extra_traversal_rec(root, given_sum, current_path):
    if root is None:
        return 0

    current_path.append(root.val)
    path_sum, path_count = 0, 0
    # This for loop is important to consider.
    # for p in current_path won't work
    for i in range(len(current_path) - 1, -1, -1):
        path_sum += current_path[i]
        if path_sum == given_sum:
            print(current_path)
            path_count += 1

    path_count += count_paths_no_extra_traversal_rec(root.left, given_sum, current_path)
    path_count += count_paths_no_extra_traversal_rec(root.right, given_sum, current_path)

    current_path.pop()

    return path_count


def main():
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(4)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(-2)
    root.left.left.left = TreeNode(-1)
    # print("Tree has paths: " + str(count_paths(root, -2)))
    print("Tree has paths: " + str(count_paths_no_extra_traversal(root, -2)))


main()
