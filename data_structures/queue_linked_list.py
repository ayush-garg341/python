from custom_ds_exceptions import QueueEmptyException

class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

      

class Queue:


    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0


    def enqueue(self, elt):
        self.len += 1
        new_node = Node(elt)
        if self.tail == None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        if self.head == None:
            self.head = new_node


    def dequeue(self):
        try:
            if self.head == None:
                raise QueueEmptyException
            temp_node = self.head.next
            self.head = temp_node   
        except QueueEmptyException:
            print("Queue is already empty")


    def front(self):
        try:
            if self.head == None:
                raise QueueEmptyException
            return self.head.data
        except QueueEmptyException:
            print("Queue is already empty")


    def is_empty(self):
        return self.head == None


    def size(self):
        return self.len

