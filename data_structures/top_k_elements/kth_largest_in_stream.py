"""
Design a class to efficiently find the Kth largest element in a stream of numbers.
The class should have the following two things:
    1. The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
    2. The class should expose a function add(int num) which will store the given number and return the Kth largest number.
"""

import heapq


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.initialize_heap()

    def initialize_heap(self):
        min_heap = []
        for num in self.nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > self.k:
                heapq.heappop(min_heap)

        self.min_heap = min_heap

    def add(self, num):
        heapq.heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
