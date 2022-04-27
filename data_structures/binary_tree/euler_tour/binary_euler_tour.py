from euler_tour_abc import EulerTour


class BinaryEulerTour(EulerTour):
    """
    Abstract base class for performing Euler tour of binary tree.
    This includes an additional _hook_invisit that is called after the tour
    of the left subtree, yet before the tour of right subtree.
    Note: Right child is always assigned index 1, even if no left sibling.
    """

    def _tour(self, p, d, path):
        result = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            result[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()

        self._hook_invisit(p, d, path)

        if self._tree.right(p) is not None:
            path.append(1)
            result[1] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()

        ans = self._hook_postvisit(p, d, path, result)
        return ans

    def _hook_invisit(self, p, d, path):
        pass
