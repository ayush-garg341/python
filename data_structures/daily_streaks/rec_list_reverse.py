"""
Given a singly linked list, reverse it in place and return the new head.
"""


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


def recursive_list_reversal(head):
    head = rec_list_reversal(head, None)
    return head


def rec_list_reversal(head, prev):
    if head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        return rec_list_reversal(head, prev)
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = recursive_list_reversal(head)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
