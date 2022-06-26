"""
Design a class that simulates a Stack data structure, implementing the following two operations:
1. push(int num): Pushes the number ‘num’ on the stack
2. pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.


example1:
    After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

    1. pop() should return 2, as it is the most frequent number
    2. Next pop() should return 1
    3. Next pop() should return 2
"""

import heapq


class Element:
    def __init__(self, number, frequency, sequence):
        self.number = number
        self.frequency = frequency
        self.sequence = sequence

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        else:
            return self.sequence > other.sequence


class FrequencyStack:
    def __init__(self):
        self.freq_map = {}
        self.max_heap = []
        self.time = 0

    def push(self, num):
        self.freq_map[num] = self.freq_map.get(num, 0) + 1
        heapq.heappush(self.max_heap, Element(num, self.freq_map[num], self.time))
        self.time += 1

    def pop(self):
        elt = heapq.heappop(self.max_heap)
        self.freq_map[elt.number] -= 1
        # if self.freq_map[elt.number] == 0:
        # del self.freq_map[elt.number]
        return elt.number


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
