class Tree:
    """Abstract base class representing a tree structure."""

    class Position:
        """An abstraction representing the location of single element."""

        def element(self):
            """Return the element stored at this position."""
            raise NotImplementedError("Must be implemented by sub class")

        def __eq__(self, other):
            """Return True if other position represent the same location."""
            raise NotImplementedError("Must be implemented by sub class")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    def root(self):
        """Return position representing the root element."""
        raise NotImplementedError("Must be implemented by sub class")

    def parent(self, p):
        """Return position representing p's parent."""
        raise NotImplementedError("Must be implemented by sub class")

    def num_children(self, p):
        """Return the number of children that position p has."""
        raise NotImplementedError("Must be implemented by sub class")

    def children(self, p):
        """Return the iteration of positions representing p's children."""
        raise NotImplementedError("Must be implmented by sub class")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("Must be implemented by sub class")

    def is_root(self, p):
        """Return True if position p is root."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if position p is leaf."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating position p from root."""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """Return the height of subtree rooted at position p."""
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of subtree rooted at position p
        If p is None, return the height of entire tree."""
        if p is None:
            p = self.root()
        return self._height(p)
