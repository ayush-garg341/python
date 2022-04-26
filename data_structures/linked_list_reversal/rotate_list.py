"""
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
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


def rotate_list(head, k):
    if head is None or head.next is None or k == 0:
        return head
    temp = head
    length = 0
    last_node = head
    while temp is not None:
        length += 1
        last_node = temp
        temp = temp.next

    k = k % length
    if k == 0:
        return head
    link_break = length - k
    i = 1
    break_pos = head
    while i != link_break:
        break_pos = break_pos.next
        i += 1

    new = break_pos.next
    break_pos.next = None
    last_node.next = head

    return new


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("Nodes of original LinkedList are: ", end="")
head.print_list()
result = rotate_list(head, 3)
print("Nodes of rotated LinkedList are: ", end="")
result.print_list()
