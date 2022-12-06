"""
Given a binary tree, convert it to doubly linked list.
"""


class Node:
    """Class Node"""

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


prev = None
head = None


def btToDll(root):
    btToDllRecursive(root)
    return head


def btToDllRecursive(root):
    if root is None:
        return
    btToDllRecursive(root.left)
    val = root.data
    global prev
    global head
    if prev is None:
        prev = Node(val)
        head = prev
    else:
        current = Node(val)
        prev.right = current
        current.left = prev
        prev = current
    btToDllRecursive(root.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

print(btToDll(root))
