"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the
root node to the nearest leaf node.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return -1
    min_depth = 0
    deq = []
    deq.append(root)
    while len(deq):
        size = len(deq)
        min_depth += 1
        while size != 0:
            pop = deq.pop(0)
            size -= 1
            if not pop.left and not pop.right:
                return min_depth
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)

    return min_depth


def find_max_depth(root):
    if root is None:
        return -1
    min_depth = 0
    deq = []
    deq.append(root)
    while len(deq):
        size = len(deq)
        min_depth += 1
        while size != 0:
            pop = deq.pop(0)
            size -= 1
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)

    return min_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    print("Tree Max Depth: " + str(find_max_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    print("Tree Max Depth: " + str(find_max_depth(root)))


main()
