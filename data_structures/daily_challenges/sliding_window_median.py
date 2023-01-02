"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’
sized sub-arrays (or windows) of the array.

example_1:
    Input: nums=[1, 2, -1, 3, 5], k = 2
    Output: [1.5, 0.5, 1.0, 4.0]

example_2:
    Input: nums=[1, 2, -1, 3, 5], k = 3
    Output: [1.0, 2.0, 3.0]
"""

import heapq


class SlidingWindowMedian:
    min_heap = []
    max_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []
        # TODO: Write your code here
        for i in range(len(nums) - k + 1):
            for j in range(i, i + k):
                num = nums[j]
                if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
                    heapq.heappush(self.max_heap, -num)
                else:
                    heapq.heappush(self.min_heap, num)
                if len(self.max_heap) > len(self.min_heap) + 1:
                    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                elif len(self.min_heap) > len(self.max_heap) + 1:
                    heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            if len(self.min_heap) > len(self.max_heap):
                result.append(self.min_heap[0])
            elif len(self.max_heap) > len(self.min_heap):
                result.append(-self.max_heap[0])
            else:
                result.append((self.min_heap[0] - self.max_heap[0]) / 2)
            self.min_heap = []
            self.max_heap = []
        return result

    def find_sliding_window_median_optimized(self, nums, k):
        result = []
        for i in range(len(nums)):
            num = nums[i]
            if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

            self.rebalance()

            if i - k + 1 >= 0:
                if len(self.max_heap) > len(self.min_heap):
                    result.append(-self.max_heap[0])
                else:
                    result.append((self.min_heap[0] - self.max_heap[0]) / 2)

                element_to_be_removed = nums[i - k + 1]
                if element_to_be_removed <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element_to_be_removed)
                else:
                    self.remove(self.min_heap, element_to_be_removed)

                self.rebalance()
        return result

    def remove(self, heap, num):
        idx = heap.index(num)
        heap[idx] = heap[-1]
        del heap[-1]
        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median_optimized(
        [1, 2, -1, 3, 5], 2
    )
    print("Sliding window medians are: " + str(result))

    # slidingWindowMedian = SlidingWindowMedian()
    # result = slidingWindowMedian.find_sliding_window_median_optimized(
    # [1, 2, -1, 3, 5], 3
    # )
    # print("Sliding window medians are: " + str(result))


main()
