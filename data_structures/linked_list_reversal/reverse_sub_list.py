"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
"""


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    # TODO: Write your code here
    i = 1
    before_p = None
    before_temp = head
    while i != p:
        before_p = before_temp
        before_temp = before_temp.next
        i += 1

    print("before temp ", before_temp.value)
    prev = None
    i = 1
    temp_head = before_temp
    print(q - p + 1)
    while i <= q - p + 1:
        temp = temp_head.next
        temp_head.next = prev
        prev = temp_head
        temp_head = temp
        i += 1

    if before_p is not None:
        before_p.next = prev
    else:
        head = prev

    before_temp.next = temp_head

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Nodes of original LinkedList are: ", end="")
head.print_list()
result = reverse_sub_list(head, 2, 4)
print("Nodes of reversed LinkedList are: ", end="")
result.print_list()
