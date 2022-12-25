"""
Author:- Ayush Garg
Description:- Circular Linked list, next pointer of last node pointing to first node.
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            new_node = Node(data)
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_last(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            new_node = Node(data)
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def delete_at_front(self):
        if self.head == None:
            print("List is empty, can not delete")
        else:
            temp = self.head
            temp_2 = self.head
            if temp.next == self.head:
                self.head = None
                return
            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next
            del temp_2

    def delete_at_last(self):
        if self.head == None:
            print("List is empty, can not delete")
        else:
            temp = self.head
            node_to_be_deleted = None
            if temp.next == self.head:
                self.head = None
                return
            while temp.next != self.head:
                node_to_be_deleted = temp
                temp = temp.next

            node_to_be_deleted.next = self.head
            del temp

    def traverse_cll(self):
        if self.head == None:
            return []
        elts = []
        temp = self.head
        if temp.next == self.head:
            elts.append(temp.data)
            return elts
        else:
            while temp.next != self.head:
                elts.append(temp.data)
                temp = temp.next
            elts.append(temp.data)
            return elts


cll = CircularLinkedList()
cll.insert_at_front(10)
# [10]
cll.insert_at_front(30)
# [30, 10]
cll.insert_at_front(20)
# [20, 30, 10]
cll.insert_at_last(40)
# [20, 30, 10, 40]
cll.insert_at_last(5)
# [20, 30, 10, 40, 5]

print(cll.traverse_cll())
cll.delete_at_front()
# [30, 10, 40, 5]
cll.delete_at_last()
# [30, 10, 40]
print(cll.traverse_cll())

cll.delete_at_front()
# [10, 40]
cll.delete_at_front()
# [40]
print(cll.traverse_cll())

cll.delete_at_front()
# []
print(cll.traverse_cll())
