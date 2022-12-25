"""
Given a binary tree, a target value of a node that's contained in the tree and a positive integer k. Write a fun that returns the value of all nodes,
that are exactly distance k from the node with target value.
"""


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = Tree(1)
tree.left = Tree(2)
tree.left.left = Tree(4)
tree.left.right = Tree(5)

tree.right = Tree(3)
tree.right.right = Tree(6)
tree.right.right.left = Tree(7)
tree.right.right.right = Tree(8)


tree2 = Tree(1)
tree2.left = Tree(2)
tree2.left.left = Tree(4)
tree2.right = Tree(3)
tree2.right.left = Tree(5)
tree2.right.right = Tree(6)
tree2.right.right.right = Tree(7)
tree2.right.right.right.right = Tree(8)


def level_order_traversal_wrong(root, target, k):
    queue = []
    queue.append({"node": root, "dir": "up"})
    level = -1
    target_level = -1
    level_order_elts = []
    while len(queue):
        size = len(queue)
        temp_res = []
        level += 1
        while size != 0:
            node = queue.pop(0)
            root = node["node"]
            direc = node["dir"]
            size -= 1
            temp_res.append({"value": root.value, "dir": direc})

            if root.value == target:
                target_level = level
                direc = "down"

            if root.left is not None:
                queue.append({"node": root.left, "dir": direc})
            if root.right is not None:
                queue.append({"node": root.right, "dir": direc})

        level_order_elts.append(temp_res)

    print(level_order_elts)

    result = []

    for i in range(len(level_order_elts)):
        for elts in level_order_elts[i]:
            if elts["value"] != target:
                if elts["dir"] == "up":
                    if target_level + i == k:
                        result.append(elts["value"])
                else:
                    if i - target_level == k:
                        result.append(elts["value"])

    return result


# print(level_order_traversal_wrong(tree, 3, 2))
# print(level_order_traversal_wrong(tree2, 8, 6))
