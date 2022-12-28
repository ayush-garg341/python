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


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
