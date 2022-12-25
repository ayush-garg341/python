"""
    Quick Sort:-
    Properties:
        In place
        Partition
        Recursive
        Divide and conquer
        All elements are distinct in an array
"""


class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def exchange(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def partition(self, low, high) -> int:
        # taking pivot as the 0th element
        pivot = self.arr[low]
        i = low + 1
        j = high
        while True:
            while self.arr[i] < pivot:
                # as long as left hand element is smaller than pivot keep increasing the index until left hand element is greater than pivot. At that point exchange the pivot with that element.
                i = i + 1
                if i >= high:
                    break

            while self.arr[j] > pivot:
                # as long as right hand element is greater than pivot keep decreasing the index until right hand element is smaller than pivot. At that point exchange the pivot with that element.
                j = j - 1
                if j <= low:
                    break

            if i < j:
                self.exchange(i, j)
            else:
                break

        self.exchange(low, j)
        # at this step pivot element will be at its right position, which means all smaller elements to the left and all greater elements to the right
        return j

    def quick_sort(self, low, high):
        if low < high:
            partition_index = self.partition(low, high)
            self.quick_sort(low, partition_index - 1)
            self.quick_sort(partition_index + 1, high)

    def print_elements(self):
        for elt in self.arr:
            print(elt, end=" ")
        print("===")


arr = [10, 5, 8, 3, 4, 9, 2, 1]

qs = QuickSort(arr)
qs.quick_sort(0, len(arr) - 1)
qs.print_elements()
