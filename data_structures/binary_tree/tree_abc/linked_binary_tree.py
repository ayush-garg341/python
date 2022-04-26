from binary_tree_abc import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated Node, if position p is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type.")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")

        return p._node

    def _make_position(self, node):
        """Return position instance for given node or None if no node."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the total number of nodes in the binary tree"""
        return self._size

    def root(self):
        """Return the root position of the tree"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of p's left child (or None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child (or None if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1

        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position
        Raise ValueError if tree is not empty"""
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Postion p, storing element e
        Return the Postion of new node.
        Raise ValueError if Postion p is invalid or if p has already left child."""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exists.")
        self._size += 1
        node._left = self.Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for position p, storing element e
        Return the position of new node
        Raise ValueError if Postion p is invalid or if p has already right child."""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists.")
        self._size += 1
        node._right = self.Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old_element = node._element
        node._element = e
        return old_element

    def _delete(self, p):
        """Delete the element at position p, and replace it with any of its child.
        Return the element that had been stored at p
        Raise ValueError if position p is invalid or if p has two child."""
        node = self._validate(p)
        if node._left and node._right:
            raise ValueError("Postion p has 2 child")
        parent = node._parent
        if node is self._root:
            self._root = node._left if node._left else node._right
        if node._left is not None:
            parent._left = node._left
            node._left._parent = parent
        elif node._right is not None:
            parent._right = node._right
            node._right._parent = parent

        self._size -= 1
        node._parent = node
        return node._element

    def preOrder(self):
        """Generate a preorder iteration of positions"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Preorder iterations of position in subtree rooted at p"""
        yield p  # return to the caller
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postOrder(self):
        """Generate a postorder iteration of positions"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p"""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def inorder(self):
        """Generating inorder iteration of positions"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generating inorder iteration of positions in subtree rooted at p"""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p

        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def breadth_first(self):
        root = self.root()
        q = []
        q.append(root)
        while len(q):
            deq = q.pop(0)
            yield deq
            for c in self.children(deq):
                q.append(c)

    def preorder_indent(self):
        """Generate indented preorder traversal of subtree rooted at p"""
        if self._root:
            for p in self._preorder_indent(self.root(), 0):
                yield p

    def _preorder_indent(self, p, d):
        """Generate indented recursive preorder traversal of subtree rooted at p"""
        yield (2 * d * " " + p.element())
        for child in self.children(p):
            for other in self._preorder_indent(child, d + 1):
                yield other

    def preorder_indent_with_numbering(self):
        """Generate pre-order indent with numbering"""
        if not self.is_empty():
            for p in self._preorder_indent_with_numbering(self.root(), 0, []):
                yield p

    def _preorder_indent_with_numbering(self, p, d, path):
        """Generate indented preordering with numbering"""
        idx = ".".join([str(p + 1) for p in path])
        yield (2 * d * " " + idx + " " + p.element())
        path.append(0)
        for child in self.children(p):
            for other in self._preorder_indent_with_numbering(child, d + 1, path):
                yield other
            path[-1] += 1
        path.pop()
