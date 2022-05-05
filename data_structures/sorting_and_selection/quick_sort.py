class QuickSortLinkedQueue:
    """
    Quick Sorting of queue implemented using LinkedList.
    - Divide -> Select a specific element x from S, which is called pivot. ( last element in S )
        - L, storing the elements in S less than x
        - E, storing the elements in S equal to x
        - G, storing the elements in S greater than x
    - Conquer -> Recursively sort sequences L and G
    - Combine -> Put back the elements in S in order.
        - First L
        - Then E
        - Then G
    """

    def __init__(self):
        pass

    def quick_sort(self, S):
        n = len(S)
        if n < 2:
            return

        L = LinkedQueue()
        E = LinkedQueue()
        G = LinkedQueue()

        pivot = S.first()

        while not S.is_empty():
            if S.first < pivot:
                L.enqueue(S.dequeue())
            elif S.first > pivot:
                G.enqueue(S.dequeue())
            else:
                E.enqueue(S.dequeue())

        self.quick_sort(L)
        self.quick_sort(G)

        while not L.is_empty():
            S.enqueue(L.dequeue())
        while not E.is_empty():
            S.enqueue(E.dequeue())
        while not G.is_empty():
            S.enqueue(G.dequeue())


class QuickSort:
    """
    Quick sort of python list.
    pivot -> randomly choosing
        - Median of three ( front, middle, tail ) -> much better and less overhead.
    """

    def __init__(self):
        pass

    def quick_sort(self, nums):
        n = len(nums)
        self.in_place_quick_sort(nums, 0, n - 1)

    def in_place_quick_sort(self, nums, low, high):
        """
        Choosing pivot as last element.
        """
        if low >= high:
            return

        pivot = nums[high]
        left = low
        right = high - 1

        while left <= right:

            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        nums[left], nums[high] = nums[high], nums[left]

        self.in_place_quick_sort(nums, low, left - 1)
        self.in_place_quick_sort(nums, left + 1, high)


if __name__ == "__main__":
    qs = QuickSort()
    nums = [85, 24, 63, 45, 17, 31, 96, 50]
    qs.quick_sort(nums)
    print("sorted = ", nums)

    nums = [-1, -5, -3, -4, -2]
    qs.quick_sort(nums)
    print("sorted = ", nums)
