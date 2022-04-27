# Pre-order traversals ( NLR )

"""
Algorithm preOrder(T, p):
    perform the "visit" action for position p
    for each child c in T.children(p) do:
        preOrder(T, c)
"""


# Post-order traversals ( LRN )

"""
Algorithm postOrder(T, p):
    for each child c in T.children(p) do:
        postOrder(T, c)
    perform the "visit" action for position p
"""

# Breadth First traversal

"""
Algorithm breadthFirst(T):
    Initialize queue Q to containe T.root()
    while Q not empty do:
        p = Q.dequeue()
        perform the "visit" action for position p
        for each child c in T.children(p) do:
            Q.enqueue(c)
"""

# in-order traversal only for binary tree ( LNR )

"""
Algorithm inOrder(T, p):
    if p has left child lc:
        inOrder(T, lc)

    perform the "visit" action for position p

    if p has right child rc:
        inOrder(T, rc)
"""


# Computing disk space with postorder traversal, internal nodes representing directories and leaves are files.
"""
def compute_space(root):
    total = root.element().space()
    for child in self.children(root):
        total += compute_space(child)
    return total
"""
