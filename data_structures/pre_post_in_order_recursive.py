class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = Node(15)
root.left = Node(12)
root.right = Node(20)
root.left.left = Node(9)
root.left.right = Node(14)
root.right.left = Node(18)
root.right.right = Node(22)

in_order_traversal = []
def inOrder(root):
    """
        Left -> Node -> Right
    """
    if root == None:
        return
    inOrder(root.left)
    in_order_traversal.append(root.data)
    inOrder(root.right)

inOrder(root)
print("in order traversal => ", in_order_traversal)


pre_order_traversal = []
def preOrder(root):
    """
        Node -> Left -> Right
    """
    if root == None:
        return 
    pre_order_traversal.append(root.data)
    preOrder(root.left)
    preOrder(root.right)

preOrder(root)
print("pre order traversal => ", pre_order_traversal)


post_order_traversal = []
def postOrder(root):
    """
        Left -> Right -> Node
    """
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    post_order_traversal.append(root.data)

postOrder(root)
print("post order traversal => ", post_order_traversal)