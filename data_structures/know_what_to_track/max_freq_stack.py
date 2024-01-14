"""
Design a stack-like data structure. You should be able to push elements to this
data structure and pop elements with maximum frequency.

You’ll need to implement the FreqStack class:-

Init(): This is a constructor used to declare a frequency stack.
Push(value): This is used to push an integer data onto the top of the stack.
Pop(): This is used to remove and return the most freq element in the stack.
"""

from collections import defaultdict


class FreqStack:
    def __init__(self):
        # Write your code here
        self.freq_map = defaultdict(int)
        self.max_freq = 0
        self.group_freq = defaultdict(list)

    def push(self, value):
        # Write your code here
        freq = self.freq_map[value] + 1
        self.freq_map[value] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        self.group_freq[freq].append(value)

    def pop(self):
        # Replace this plaecholder return statement with your code
        elt = self.group_freq[self.max_freq].pop()
        self.freq_map[elt] -= 1
        if not self.group_freq[self.max_freq]:
            self.max_freq -= 1
        return elt


freq = FreqStack()
freq.push(5)
freq.push(7)
freq.push(7)
freq.push(5)
print(freq.pop())
