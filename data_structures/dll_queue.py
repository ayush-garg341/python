"""
    Queue: FIFO
    First In first out
"""

from doubly_linked_list import DoublyLinkedList


class DLLQueue:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def insert(self, elt):
        self.dll.insert_at_last(elt)

    def front(self):
        return self.dll.front()

    def pop(self):
        self.dll.remove_from_front()

    def length(self):
        return self.dll.size()

    def is_empty(self):
        return self.dll.is_empty()

    def print_elts(self):
        return self.dll.forward_traverse()


queue = DLLQueue()
queue.insert(5)
queue.insert(10)
queue.insert(20)
queue.insert(21)
print("Elements in a queue => ", queue.print_elts())
print("Front element of a queue => ", queue.front())
queue.pop()
print("After popping elements in a queue => ", queue.print_elts())
print("After popping front element => ", queue.front())
print(queue.length())
