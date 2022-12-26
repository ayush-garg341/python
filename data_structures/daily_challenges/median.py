"""
Design a class to calculate the median of a number stream. The class should
    have the following two methods:
    - insertNum(int num): stores the number in the class
    - findMedian(): returns the median of all numbers inserted in the class
"""

import heapq


class MedianOfAStream:
    min_heap = []
    max_heap = []

    def insert_num(self, num):
        # TODO: Write your code here
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            if len(self.max_heap) > len(self.min_heap) + 1:
                top = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -top)
        else:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap) + 1:
                top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -top)

    def find_median(self):
        # TODO: Write your code here
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(8)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(6)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
