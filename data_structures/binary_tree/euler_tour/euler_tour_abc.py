"""
Template method pattern: Object oriented Software design pattern.
The template method pattern describe a generic computation mechanism that can be specialized
for a particular application by redifining certain steps.

pre-visit hook -> called before subtrees are traversed.
post-visit hook -> called after subtrees are traversed.
"""


class EulerTour:
    """Abstract base class for performing Euler tour of tree
    _hook_previsit and _hook_postvisit may be over-ridden by sub-class.
    """

    def __init__(self, tree):
        """Prepare an euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of the root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position P

        p:- Position of current node being visited.
        d:- depth of p in the tree.
        path:- list of indices of children on path from root to p
        """

        self._hook_previsit(p, d, path)
        path.append(0)
        results = []
        for child in self._tree.children(p):
            results.append(self._tour(child, d + 1, path))
            path[-1] += 1

        path.pop()
        ans = self._hook_postvisit(p, d, path, results)
        return ans

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreOrderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2 * d * " " + p.element())


class PreOrderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = ".".join(str(j + 1) for j in path)
        print(2 * d * " " + label, p.element())


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(",", end="")
        print(p.element())
        if not self._tree.is_leaf(p):
            print("(", end="")

    def _hook_postvisit(self, p, d, path, results):
        if not self._tree.is_leaf(p):
            print(")", end="")
