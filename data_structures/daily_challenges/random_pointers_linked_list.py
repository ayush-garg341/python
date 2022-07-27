"""
Given a linkedlist with Node having three parts i.e data, next pointer and random pointer.
Clone this linked list.
"""

class Node:

    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random



class CloneLinkedList:

    def __init__(self, head):
        self.head = head
        self.random_ptr_map = {}
        self.corresponding_map = {}

    def clone(self):
        head = self.head
        temp = new_head = None
        while head is not None:
            if temp is None:
                temp = Node(head.data, None, None)
                new_head = temp
            else:
                temp.next = Node(head.data, None, None)
                temp = temp.next

            self.random_ptr_map[temp] = head.random
            self.corresponding_map[head] = temp
            head = head.next

        head = new_head
        while new_head is not None:
            random_pointer = self.random_ptr_map[new_head]
            if random_pointer:
                new_head.random = self.corresponding_map[random_pointer]

            new_head = new_head.next

        return head




node1 = Node(1, None, None)
node2 = Node(2, None, None)
node3 = Node(3, None, None)
node4 = Node(4, None, None)

head = node1

node1.next = node2
node1.random = node3
node2.next = node3
node2.random = node4
node3.next = node4

cloned_ll = CloneLinkedList(head)
new_head = cloned_ll.clone()

while new_head is not None:
    print(new_head.data)
    if new_head.random:
        print(new_head.random.data)

    print()
    new_head = new_head.next


