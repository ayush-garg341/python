"""
Serialize a binary tree to a file ( in the form of string )
Deserialize a string into binary tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        self.serialize_rec(root, data)
        return ",".join(data)

    def serialize_rec(self, root, data):
        if root is None:
            data.append("*")
            return
        data.append(str(root.val))
        self.serialize_rec(root.left, data)
        self.serialize_rec(root.right, data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        data.reverse()
        root = self.deserialize_rec(data)
        return root

    def deserialize_rec(self, data):
        if len(data):
            val = data.pop()
            if val == "*":
                return None

            root = TreeNode(val)
            root.left = self.deserialize_rec(data)
            root.right = self.deserialize_rec(data)
            return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class SecondSolution:
    preorderIdx = 0

    def serialize(self, root):
        """Encodes a tree to a single string
        :type root: TreeNode
        :rtype str
        """
        inorder = []
        self.inorder_traversal(root, inorder)
        preorder = []
        self.preorder_traversal(root, preorder)
        print(inorder, preorder)
        return ",".join(inorder) + "-" + ",".join(preorder)

    def inorder_traversal(self, root, data):
        if root is None:
            return
        self.inorder_traversal(root.left, data)
        data.append(str(root.val))
        self.inorder_traversal(root.right, data)

    def preorder_traversal(self, root, data):
        if root is None:
            return
        data.append(str(root.val))
        self.preorder_traversal(root.left, data)
        self.preorder_traversal(root.right, data)

    def deserialize(self, data: str):
        """Decodes a string into tree root.
        :type data: str
        :rtype root: TreeNode
        """
        data = data.split("-")
        inorder = data[0].split(",")
        inorder_dict = dict()
        for i in range(len(inorder)):
            inorder_dict[int(inorder[i])] = i
        preorder = data[1].split(",")
        for i in range(len(preorder)):
            preorder[i] = int(preorder[i])
        print(preorder, inorder_dict)
        root = self.decode(inorder_dict, preorder, 0, len(inorder) - 1)
        return root

    def decode(self, inorder, preorder, inorder_start, inorder_end):
        if inorder_end - inorder_start < 0:
            return None

        val = preorder[self.preorderIdx]
        root = TreeNode(val)
        inorder_idx = inorder[val]
        self.preorderIdx += 1

        root.left = self.decode(inorder, preorder, inorder_start, inorder_idx - 1)
        root.right = self.decode(inorder, preorder, inorder_idx + 1, inorder_end)

        return root


root = TreeNode(100)
root.left = TreeNode(50)
root.left.left = TreeNode(25)
root.left.right = TreeNode(75)
root.right = TreeNode(200)
root.right.right = TreeNode(350)

soln = SecondSolution()
data = soln.serialize(root)
rootNode = soln.deserialize(data)
print(rootNode.val)
print(rootNode.left.val)
print(rootNode.left.left.val)
print(rootNode.left.right.val)
print(rootNode.right.val)
print(rootNode.right.right.val)
