"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

example1:
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
    Output: true

example2:
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
    Output: false
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


def is_palindrome(head):
    if head is None or head.next is None:
        return True
    print_list(head)
    temp = head
    flag = True
    middle_node = find_middle_of_linked_list(head)
    reverse_head = reverse_linked_list(middle_node)
    reverse_head_copy = reverse_head

    while head is not None and reverse_head is not None:
        if head.value != reverse_head.value:
            flag = False
            break

        head = head.next
        reverse_head = reverse_head.next

    reverse_head = reverse_linked_list(reverse_head_copy)

    print_list(temp)

    if flag:
        return True
    return False


def find_middle_of_linked_list(head):
    if head is None or head.next is None:
        return head
    slow = head.next
    fast = head.next.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return slow

    return slow


def print_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print("\n")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(is_palindrome(head))


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

print(is_palindrome(head))

head.next.next.next.next.next = Node(2)

print(is_palindrome(head))
