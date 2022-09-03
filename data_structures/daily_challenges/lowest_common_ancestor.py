"""
Given a binary tree and two nodes n1, n2 find the common ancestor.
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


def lowest_common_ancestor_using_path_approach(root, n1, n2):
    found = False
    path1 = []
    path_from_root_to_node(root, n1, path1)

    path2 = []
    path_from_root_to_node(root, n2, path2)

    print(path1, path2)
    for i in range(len(path1)-1, -1, -1):
        for j in range(len(path2)-1, -1, -1):
            last_elt = path1[i]
            if last_elt == path2[j]:
                lca = last_elt
                found = True
                break
        if found:
            break
    if found:
        print(lca)
    else:
        print("No Common ancestor")

def path_from_root_to_node(root, n, path):
    if root is None:
        return False
    if root.value == n:
        path.append(n)
        return True

    path.append(root.value)

    if path_from_root_to_node(root.left, n, path) or path_from_root_to_node(root.right, n, path):
        return True
    else:
        path.pop()

# path = []
# path_from_root_to_node(tree, 5, path)
# print(path)
# path = []
# path_from_root_to_node(tree, 7, path)
# print(path)
# path = []
# path_from_root_to_node(tree, 15, path)
# print(path)

lowest_common_ancestor_using_path_approach(tree, 4, 7)
lowest_common_ancestor_using_path_approach(tree2, 5, 8)
