
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


def preOrder(root):
    pre_order_traversal = []
    stack = []
    if root == None:
        return pre_order_traversal
    
    stack.append(root)
    pre_order_traversal.append(root.data)
    root = root.left
    while stack or root!=None:
        if root != None:
            pre_order_traversal.append(root.data)
            stack.append(root)
            root = root.left
        else:
            top = stack[-1]
            stack.pop()
            root = top.right

    return pre_order_traversal

pre_order_traversal =  preOrder(root)
print("pre order iterative traversal => ", pre_order_traversal)


def inOrder(root):
    in_order_traversal = []
    stack = []
    if root == None:
        return in_order_traversal
    
    stack.append(root)
    root = root.left
    while stack or root != None:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            top = stack[-1]
            stack.pop()
            in_order_traversal.append(top.data)
            root = top.right
    
    return in_order_traversal

in_order_traversal = inOrder(root)
print("in order iterative traversal => ", in_order_traversal)


def postOrder(root):
    stack1 = []
    stack2 = []
    post_order_traversal = []
    stack1.append(root)
    while stack1:
        top = stack1[-1]
        stack1.pop()
        stack2.append(top.data)
        if top.left != None:
            stack1.append(top.left)
        if top.right != None:
            stack1.append(top.right)

    while stack2:
        post_order_traversal.append(stack2[-1])
        stack2.pop()

    return post_order_traversal


post_order_traversal = postOrder(root)
print("post order iterative traversal => ", post_order_traversal)