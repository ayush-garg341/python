from custom_ds_exceptions import LinkedListEmptyException

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__len = 0


    def insert_at_front(self, data):
        self.__len += 1
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        if self.tail == None:
            self.tail = new_node


    def insert_at_last(self, data):
        self.__len += 1
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        if self.head == None:
            self.head = new_node


    def remove_from_front(self):
        try:
            if self.head == None:
                raise LinkedListEmptyException("Linked List is empty")
            temp = self.head
            if self.head == self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
            self.__len -= 1
            del temp
        except LinkedListEmptyException as emptyerr:
            print(emptyerr)


    def remove_from_last(self):
        try:
            if self.tail == None:
                raise LinkedListEmptyException("Linked List is empty")

            temp = self.tail
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.__len -= 1
            del temp
        except LinkedListEmptyException as emptyerr:
            print(emptyerr)


    def front(self):
        try:
            if self.head == None:
                raise LinkedListEmptyException("Linked List is empty")
            return self.head.data
        except LinkedListEmptyException as emptyerr:
            print(emptyerr)


    def last(self):
        try:
            if self.tail == None:
                raise LinkedListEmptyException("Linked List is empty")
            return self.tail.data
        except LinkedListEmptyException as emptyerr:
            print(emptyerr)


    def forward_traverse(self):
        elts = []
        temp = self.head
        while temp != None:
            elts.append(temp.data)
            temp = temp.next        
        return elts


    def backward_traverse(self):
        elts = []
        temp = self.tail
        while temp != None:
            elts.append(temp.data)
            temp = temp.prev  
        return elts

    
    def is_empty(self):
        return self.head == None or self.tail == None

    
    def size(self):
        return self.__len
