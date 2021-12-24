"""
    Stack: LIFO
    Last In First Out
"""

from doubly_linked_list import DoublyLinkedList

class DLLStack:
    def __init__(self):
        self.dll = DoublyLinkedList()


    def insert(self, elt):
        self.dll.insert_at_last(elt)


    def last(self):
        return self.dll.last()


    def pop(self):
        self.dll.remove_from_last()


    def length(self):
        return self.dll.size()


    def is_empty(self):
        return self.dll.is_empty()


    def print_elts(self):
        return self.dll.forward_traverse()


stack = DLLStack()

stack.insert(10)
stack.insert(5)
stack.insert(8)
stack.insert(6)
print(stack.print_elts())
print(stack.last())
stack.pop()
print("After popping from stack =>",stack.print_elts())
print("After popping, last element from stack => ",stack.last())
print(stack.length())
stack.pop()
print("After popping from stack =>",stack.print_elts())
print("After popping, last element from stack => ",stack.last())
stack.pop()
stack.pop()
stack.pop()
