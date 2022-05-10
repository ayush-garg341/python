"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

example1:-
    Input: nums=[1, 2, -1, 3, 5], k = 2
    Output: [1.5, 0.5, 1.0, 4.0]
    Explanation: Lets consider all windows of size ‘2’:
    [1, 2, -1, 3, 5] -> median is 1.5
    [1, 2, -1, 3, 5] -> median is 0.5
    [1, 2, -1, 3, 5] -> median is 1.0
    [1, 2, -1, 3, 5] -> median is 4.0
"""

import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            if not self.max_heap or -self.max_heap[0] >= nums[i]:
                heapq.heappush(self.max_heap, -nums[i])
            else:
                heapq.heappush(self.min_heap, nums[i])

            self.balance_heap()
            if i - k + 1 >= 0:
                if len(self.min_heap) == len(self.max_heap):
                    result.append((self.min_heap[0] - self.max_heap[0]) / 2)
                else:
                    result.append(-self.max_heap[0] / 1.0)

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove_and_heapify(-elementToBeRemoved, self.max_heap)
                else:
                    self.remove_and_heapify(elementToBeRemoved, self.min_heap)
                self.balance_heap()
        return result

    def remove_and_heapify(self, num, heap):
        index = heap.index(num)  # find the element
        heap[index] = heap[-1]

        parent = (index - 1) // 2

        if index == len(heap) - 1:
            heap.pop()
        elif index > 0 and heap[index] < heap[parent]:
            heap.pop()
            self._upheap(heap, index)
        else:
            heap.pop()
            self._downheap(heap, index)

    def balance_heap(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def _upheap(self, heap, index):
        parent = (index - 1) // 2
        if index > 0 and heap[index] < heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            self._upheap(heap, parent)

    def _downheap(self, heap, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(heap):
            small_child = left_child

            if right_child < len(heap):
                if heap[right_child] < heap[left_child]:
                    small_child = right_child

            if heap[index] > heap[small_child]:
                heap[small_child], heap[index] = heap[index], heap[small_child]
                self._downheap(heap, small_child)


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
