"""
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
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
    before_p = None
    before_temp = head

    i = 1
    while i != p:
        before_p = before_temp
        before_temp = before_temp.next
        i += 1

    at_p = before_temp

    i = 0
    prev = before_p
    while i != q - p + 1:
        temp = before_temp.next
        before_temp.next = prev
        prev = before_temp
        before_temp = temp
        i += 1

    if before_p is not None:
        before_p.next = prev
    else:
        head = prev

    at_p.next = before_temp

    return head


def reverse_between_two_pos():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)

    n = 8
    k = 2

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    start = 1
    end = k
    while True:
        print(start, end)
        head = reverse_sub_list(head, start, end)

        start = end + 1
        end = end + k
        i = 1
        while i <= k:
            start += 1
            end += 1
            i += 1
        if start > n:
            break
        if end > n:
            end = n
    print("Nodes of reversed LinkedList are: ", end="")
    head.print_list()


reverse_between_two_pos()
