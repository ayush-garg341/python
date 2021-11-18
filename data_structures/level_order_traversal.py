from queue_linked_list import Queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(15)
root.left = TreeNode(12)
root.right = TreeNode(20)
root.left.left = TreeNode(9)
root.left.right = TreeNode(14)
root.right.left = TreeNode(18)
root.right.right = TreeNode(22)


def levelOrder(root):
    level_order_traversal = []
    if root == None:
        return level_order_traversal

    q = Queue()

    q.enqueue(root)
    while not q.is_empty():
        len = q.size()
        same_level_elts = []
        while len != 0:
            front = q.front()
            same_level_elts.append(front.data.data)
            q.dequeue()
            len -= 1
            if front.data.left != None:
                q.enqueue(front.data.left)
            if front.data.right != None:
                q.enqueue(front.data.right)

        level_order_traversal.append(same_level_elts)

    return level_order_traversal

level_order_traversal = levelOrder(root)
print("level order traversal => ", level_order_traversal)