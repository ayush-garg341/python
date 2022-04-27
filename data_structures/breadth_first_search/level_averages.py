"""
Given a binary tree, populate an array to represent the averages of all of its levels.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result
    deq = []
    deq.append(root)
    while len(deq):
        size = len(deq)
        num_nodes = size
        sum = 0
        while size != 0:
            pop = deq.pop(0)
            sum += pop.val
            size -= 1
            if pop.left:
                deq.append(pop.left)
            if pop.right:
                deq.append(pop.right)
        result.append(sum / num_nodes)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
