"""
Given pre-order traversal nodes construct the BST from it.
And return the root node.
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues) == 1:
        root = BST(preOrderTraversalValues[0], None, None)
        return root
    root = preOrderTraversalValuesRec(preOrderTraversalValues)
    return root


def preOrderTraversalValuesRec(preOrder):
    if len(preOrder) == 0:
        return
    print("preorder === ", preOrder)
    current_elt = preOrder[0]
    root = BST(current_elt)
    index = get_current_index(preOrder[0], preOrder)
    print("index = = ", index)
    root.left = preOrderTraversalValuesRec(preOrder[1:index])
    if index != -1:
        root.right = preOrderTraversalValuesRec(preOrder[index:])

    return root


def get_current_index(current_elt, preOrder):
    index = -1
    for i in range(len(preOrder)):
        if preOrder[i] > current_elt:
            index = i
            break
    return index


root = reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])

# printing pre-order traversal of bst.


def preOrder(root):
    if root is None:
        return

    print(root.value, end=" - ")
    preOrder(root.left)
    preOrder(root.right)


preOrder(root)
