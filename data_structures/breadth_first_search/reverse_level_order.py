"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e.,
the lowest level comes first.
You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    # TODO: Write your code here
    deq = []
    if root is None:
        return []
    deq.append(root)
    while len(deq):
        size = len(deq)
        temp_result = []
        while size != 0:
            pop = deq.pop(0)
            temp_result.append(pop.val)
            size -= 1
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)
        result.appendleft(temp_result)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
