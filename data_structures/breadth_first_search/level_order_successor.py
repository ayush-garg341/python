"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order
successor is the node that appears right after the given node in the level order traversal.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    # TODO: Write your code here
    if key is None or root is None:
        return None
    successor = root.val
    deq = []
    deq.append(root)
    found = False
    while len(deq):
        pop = deq.pop(0)
        if found:
            return pop
        if pop.val == key and not found:
            found = True

        if pop.left:
            deq.append(pop.left)
        if pop.right:
            deq.append(pop.right)

    return successor


def find_predecessor(root, key):
    # TODO: Write your code here
    if key is None or root is None or key == root.val:
        return None
    predecessor = root.val
    deq = []
    deq.append(root)
    while len(deq):
        pop = deq.pop(0)
        if pop.val == key:
            return predecessor
        predecessor = pop

        if pop.left:
            deq.append(pop.left)
        if pop.right:
            deq.append(pop.right)

    return predecessor


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    result2 = find_predecessor(root, 3)
    if result:
        print(result.val)
        print(result2.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    result2 = find_predecessor(root, 9)
    if result:
        print(result.val)
        print(result2.val)

    result = find_successor(root, 12)
    result2 = find_predecessor(root, 7)
    if result:
        print(result.val)
        print(result2.val)


main()
