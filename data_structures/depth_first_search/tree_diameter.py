"""
Given a binary tree, find the length of its diameter.
The diameter of a tree is the number of nodes on the longest path between any two leaf nodes.
The diameter of a tree may or may not pass through the root.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        # TODO: Write your code here
        max_diam = 0
        deq = []
        deq.append(root)
        while len(deq):
            size = len(deq)
            while size != 0:
                pop = deq.pop()
                size -= 1
                max_diam = max(
                    max_diam,
                    self.root_height_by_nodes(pop.left)
                    + self.root_height_by_nodes(pop.right),
                )
                if pop.left:
                    deq.append(pop.left)
                if pop.right:
                    deq.append(pop.right)
        return max_diam

    def root_height_by_nodes(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(
                self.root_height_by_nodes(root.left),
                self.root_height_by_nodes(root.right),
            )

    def find_diameter_without_extra_space(self, root):
        self.find_diameter_without_extra_space_rec(root)
        return self.treeDiameter

    def find_diameter_without_extra_space_rec(self, current_node):
        if current_node is None:
            return 0
        left_tree_height = self.find_diameter_without_extra_space_rec(current_node.left)
        right_tree_height = self.find_diameter_without_extra_space_rec(
            current_node.right
        )
        if left_tree_height != 0 and right_tree_height != 0:
            diameter = left_tree_height + right_tree_height + 1
            self.treeDiameter = max(self.treeDiameter, diameter)

        return max(left_tree_height, right_tree_height) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    print(
        "Tree Diameter with nodes: "
        + str(treeDiameter.find_diameter_without_extra_space(root))
    )
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    print(
        "Tree Diameter with nodes: "
        + str(treeDiameter.find_diameter_without_extra_space(root))
    )


main()
