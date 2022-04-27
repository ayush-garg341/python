"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values
of all nodes of each level from left to right in separate sub-arrays.
"""


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result
    deq = deque()
    deq.append(root)
    while len(deq):
        size = len(deq)
        temp_result = []
        while size != 0:
            pop = deq.popleft()
            size -= 1
            temp_result.append(pop.val)
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)
        result.append(temp_result)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
