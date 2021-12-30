"""
    Binary search tree insertion and deletion.
"""

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class BST:

    def __init__(self):
        self.path = []


    def search(self, root, data, paths):
        if root.data == data:
            return paths
        elif data < root.data:
            paths.append("left")
            self.search(root.left, data, paths)
        else:
            paths.append("right")
            self.search(root.right, data, paths)

        return paths


    def find_minimum_in_right_subtree(self, root):
        while(root.left!=None):
            root = root.left

        return root.data


    def find_max_in_left_subtree(self, root):
        while(root.right!=None):
            root = root.right

        return root.data


    def insert(self, root, data):
        if root == None:
            return BSTNode(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)

        return root


    def delete(self, root, data):
        if (root.data == data):
            if root.left != None and root.right != None:
                # handle the two child case
                mim_elt = self.find_minimum_in_right_subtree(root.right)
                root.data = mim_elt
                root.right = self.delete(root.right, mim_elt)
                return root
            elif root.left == None and root.right == None:
                # handle the no child case
                del root
                return None
            elif root.left==None or root.right == None:
                # handle the one child case
                if root.left == None:
                    root.data = root.right.data
                    root.right = self.delete(root.right, root.right.data)
                    return root
                elif root.right == None:
                    root.data = root.left.data
                    root.left = self.delete(root.left, root.left.data)
                    return root

        elif data < root.data:
            root.left = self.delete(root.left, data)
        else:
            root.right = self.delete(root.right, data)

        return root


root=None
bst = BST()
root = bst.insert(root, 50)
root = bst.insert(root, 40)
root = bst.insert(root, 60)
root = bst.insert(root, 30)
root = bst.insert(root, 70)
root = bst.insert(root, 45)
root = bst.insert(root, 55)
root = bst.insert(root, 48)
root = bst.insert(root, 42)
root = bst.insert(root, 65)
root = bst.insert(root, 63)

print(bst.search(root, 42, []))
print(bst.search(root, 48, []))

root = bst.delete(root, 42)
root = bst.delete(root, 45)
print(bst.search(root, 48, []))


root = bst.delete(root, 60)
print(bst.search(root, 65, []))
print(bst.search(root, 55, []))
