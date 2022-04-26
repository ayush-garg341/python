from linked_binary_tree import LinkedBinaryTree

lbt = LinkedBinaryTree()
root = lbt._add_root("Electronics R'Us")
rc1 = lbt._add_right(root, "Sales")
rc2 = lbt._add_left(rc1, "Domestic")
rc3 = lbt._add_right(rc1, "International")
rc4 = lbt._add_left(rc3, "Canada")
rc5 = lbt._add_right(rc3, "America")
lc1 = lbt._add_left(root, "R&D")

print("Indented printing")
print(" =========== ")
for p in lbt.preorder_indent():
    print(p)

print(" =========== ")
print("Indented printing with numbering")
for p in lbt.preorder_indent_with_numbering():
    print(p)
