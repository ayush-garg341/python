from linked_binary_tree import LinkedBinaryTree

lbt = LinkedBinaryTree()
root = lbt._add_root(58)
rc3 = lbt._add_right(root, 90)
rc4 = lbt._add_left(rc3, 62)
rc5 = lbt._add_right(rc4, 75)
lc1 = lbt._add_left(root, 31)
lc2 = lbt._add_left(lc1, 25)
lc5 = lbt._add_right(lc2, 28)
lc3 = lbt._add_left(lc2, 12)
rc1 = lbt._add_right(lc1, 42)
rc2 = lbt._add_left(rc1, 36)

print("pre order ", end=" = ")
for p in lbt.preOrder():
    print(p.element(), end=" ")

print()
print("post order ", end=" = ")
for p in lbt.postOrder():
    print(p.element(), end=" ")

print()
print("in order ", end=" = ")
for p in lbt.inorder():
    print(p.element(), end=" ")

print()
print("breadth first ", end=" = ")
for p in lbt.breadth_first():
    print(p.element(), end=" ")

print()
