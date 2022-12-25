"""
Given a linked list rotate/shift it by K places.
If k is pos rotate forward else backward.
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rotate(head, k):
    if not head:
        return head
    l, end = length(head)
    k = k % l
    prev = None
    main_head = head
    actual_traversal = l - k
    if actual_traversal == 0 or actual_traversal == l:
        return head
    while actual_traversal != 0:
        prev = head
        head = head.next
        actual_traversal -= 1

    temp = prev.next
    prev.next = None
    head = temp
    end.next = main_head

    return head


def length(head):
    l = 1
    while head.next:
        l += 1
        head = head.next

    return l, head


def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()


head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)

# head_copy = head
# new_head = rotate(head, 2)
# print_list(new_head)

new_head = rotate(head, -2)
print_list(new_head)
