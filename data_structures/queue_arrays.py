"""
    Implementation of queue using circular array.
    FIFO -> First in First Out
"""

from custom_ds_exceptions import QueueFullException, QueueEmptyException

class Queue:

    def __init__(self, length) -> None:

        self.front_idx = 0
        self.rear_idx = 0
        self.__len = length
        self.circular_arr = [None]*length


    def enqueue(self, elt):
        """
            Will enqueue elt in circular wrapp around fashion i.e. if rear_idx = N-1 will check if 0th index is empty.
        """
        try:
            if self.size() == self.__len - 1:
                raise QueueFullException
            
            self.circular_arr[self.rear_idx] = elt
            self.rear_idx = (self.rear_idx + 1) % self.__len

        except QueueFullException:
            print("Queue is full")


    def dequeue(self):
        """
            Will dequeue from front.
        """
        try:
            if self.is_empty():
                raise QueueEmptyException
            self.circular_arr[self.front_idx] = None
            self.front_idx = (self.front_idx + 1) % self.__len

        except QueueEmptyException:
            print("Queue is empty")


    def front(self):
        try:
            if self.is_empty():
                raise QueueEmptyException
            return self.circular_arr[self.front_idx]
        except QueueEmptyException:
            print("Queue is empty")


    def size(self):
        """
            Situations:
            1. rear_idx - front_idx < 0
            2. rear_idx - front_idx > 0
        """
        return (self.__len + self.rear_idx - self.front_idx) % self.__len


    def is_empty(self):
        return self.front_idx == self.rear_idx

