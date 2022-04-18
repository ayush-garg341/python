"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from
the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.

example1:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

example2:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    prev_head = None
    while head is not None:
        next_node = head.next
        head.next = prev_head
        prev_head = head
        head = next_node

    return prev_head


def rearrange_list(head):
    if head is None or head.next is None:
        return head
    print_list(head)
    temp = head
    middle_node = left_middle_of_linked_list(head)
    reverse_second_half = reverse_linked_list(middle_node.next)
    middle_node.next = None
    print_list(head)
    print_list(reverse_second_half)
    while head is not None and reverse_second_half is not None:
        temp_next = head.next
        reverse_next = reverse_second_half.next
        head.next = reverse_second_half
        head.next.next = temp_next
        head = temp_next
        reverse_second_half = reverse_next

    print_list(temp)


def left_middle_of_linked_list(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast is not None:
        if fast.next is None or fast.next.next is None:
            return slow
        else:
            fast = fast.next.next

        slow = slow.next

    return slow


def print_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print("\n")


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
rearrange_list(head)
