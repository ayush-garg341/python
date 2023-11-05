"""
given an array of positive integers, weights, where weights[i] is the weight of the ith index.
Write a function, Pick Index(), which performs weighted random selection to return an index from the weights array.
The larger the value of weights[i], the heavier the weight is, and the higher the chances of its index being picked.
"""
import random

class RandomPickWeights:

    def __init__(self, weights):
        self.running_sums = []
        running_sum = 0

        for w in weights:
            running_sum += w
            self.running_sums.append(running_sum)

        self.total_sum = running_sum

    def pick_index(self):
        target = random.randint(1, self.total_sum)
        low = 0
        high = len(self.running_sums) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.running_sums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return high

