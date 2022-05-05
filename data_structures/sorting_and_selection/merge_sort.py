import math


class MergeSort:
    """
    Merge sort using recursion (divide and conquer approach)
    """

    def __init__(self, nums):
        self._nums = nums

    def merge_sort(self, nums, low, high):
        """
        Recursively halving a list into two parts (left and right)
        """
        if high <= low:
            return
        mid = (low + high) // 2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        """
        Merging two sorted lists
        """
        aux_arr = [0] * len(nums)
        i, j = low, mid + 1
        count = low
        while i <= mid and j <= high:
            if nums[i] < nums[j]:
                aux_arr[count] = nums[i]
                i += 1
            else:
                aux_arr[count] = nums[j]
                j += 1
            count += 1

        while i <= mid:
            aux_arr[count] = nums[i]
            i += 1
            count += 1

        while j <= high:
            aux_arr[count] = nums[j]
            j += 1
            count += 1

        i = low
        while i < count:
            nums[i] = aux_arr[i]
            i += 1


class MergeSortLinkedQueue:
    """
    Merge sort queue implemented as linked list (LinkedQueue).
    """

    def __init__(self):
        pass

    def merge_sort(self, s):
        n = len(s)
        if n < 2:
            return
        s1 = LinkedQueue()
        s2 = LinkedQueue()

        while len(s1) < n // 2:
            s1.enqueue(s.dequeue)
        while not s.is_empty():
            s2.enqueue(s.dequeue)

        self.merge_sort(s1)
        self.merge_sort(s2)

        self.merge(s1, s2, s)

    def merge(self, s1, s2, s):
        while not s1.is_empty() and not s2.is_empty():
            if s1.first() < s2.first():
                s.enqueue(s1.dequeue())
            else:
                s.enqueue(s2.dequeue())
        while not s1.is_empty():
            s.enqueue(s1.dequeue())
        while not s2.is_empty():
            s.enqueue(s2.dequeue())


class MergeSortNonRecursive:
    """
    Merge sort non-recrsive. Bit faster than recursive as it avoids the extra overhead of recursive calls.
    And temporary memory at each level.
    """

    def __init__(self):
        pass

    def merge_sort(self, nums):
        """
        Sort the elements of python list using merge sort.
        """
        n = len(nums)
        logn = math.ceil(math.log(n, 2))
        src = nums
        dest = [None] * len(nums)
        for i in (2**k for k in range(logn)):
            for j in range(0, n, 2 * i):
                self.merge(src, dest, j, i)

            # this is an important thing, without swapping will get wrong result since both pointing to same list.
            # src = dest
            src, dest = dest, src

        return src

    def merge(self, src, results, start, inc):
        end1 = min(start + inc, len(src))
        end2 = min(start + (2 * inc), len(src))
        x, y, z = start, start + inc, start
        while x < end1 and y < end2:
            if src[x] < src[y]:
                results[z] = src[x]
                x += 1
            else:
                results[z] = src[y]
                y += 1
            z += 1

        while x < end1:
            results[z] = src[x]
            x += 1
            z += 1

        while y < end2:
            results[z] = src[y]
            y += 1
            z += 1


if __name__ == "__main__":
    nums = [85, 24, 63, 45, 17, 31, 96, 50]
    ms = MergeSort(nums)
    ms.merge_sort(nums, 0, len(nums) - 1)
    print("merge sort recursuve = ", nums)

    ms2 = MergeSortNonRecursive()
    nums = [85, 24, 63, 45, 17, 31, 96, 50]
    nums = ms2.merge_sort(nums)
    print("merge sort iterative = ", nums)

    nums = [-4, -5, -2, -1, -3]
    ms = MergeSort(nums)
    ms.merge_sort(nums, 0, len(nums) - 1)
    print("merge sort recursive = ", nums)

    ms2 = MergeSortNonRecursive()
    nums = [-4, -5, -2, -1, -3]
    nums = ms2.merge_sort(nums)
    print("merge sort iterative = ", nums)
