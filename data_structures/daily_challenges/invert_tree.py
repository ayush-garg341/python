"""
Invert the binary tree and return the root, inverting means mirror image.
"""


def invertBinaryTree(root):
    # Write your code here.
    q = []
    q.append(root)
    while q:
        size = len(q)
        while size != 0:
            pop = q.pop(0)
            size -= 1
            if pop.left:
                q.append(pop.left)
            if pop.right:
                q.append(pop.right)

            pop.left, pop.right = pop.right, pop.left

    return root


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
