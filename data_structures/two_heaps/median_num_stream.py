"""
Design a class to calculate the median of a number stream. The class should have the following two methods:
    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class
"""

import heapq


class MedianOfAStreamInsertionSort:
    nums = []

    def insert_num(self, num):
        self.nums.append(num)

        for i in range(len(self.nums)):
            hole = i
            current_val = self.nums[i]

            while hole > 0 and self.nums[hole - 1] > current_val:
                self.nums[hole] = self.nums[hole - 1]
                hole = hole - 1
            self.nums[hole] = current_val

    def find_median(self):
        n = len(self.nums)
        if n % 2 == 0:
            index = n // 2
            return (self.nums[index] + self.nums[index - 1]) / 2
        else:
            index = n // 2
            return self.nums[index]


class MedianOfAStream:
    min_heap = []  # for storing the numbers larger than median
    max_heap = []  # for storing the numbers smaller than median

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        return -self.max_heap[0] / 1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


def main_insertion_sort():
    medianOfAStream = MedianOfAStreamInsertionSort()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
print("-----Using insertion sort--------")
main_insertion_sort()
