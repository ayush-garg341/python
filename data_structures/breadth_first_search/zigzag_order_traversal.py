"""
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right, then right to left for the next level.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result
    deq = []
    deq.append(root)
    level = 0
    while len(deq):
        level += 1
        size = len(deq)
        index = size
        temp_result = [None] * size
        while size != 0:
            pop = deq.pop(0)
            if level % 2 == 0:
                temp_result[size - 1] = pop.val
            else:
                temp_result[index - size] = pop.val
            size -= 1
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
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
