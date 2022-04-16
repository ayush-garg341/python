"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def length_cycle(head):
    node_map = {}
    count = 1
    while head is not None:
        if head not in node_map:
            node_map[head] = count
            count += 1
        else:
            return count - node_map[head]

        head = head.next


def detect_begin_node(head):
    node_map = {}
    while head is not None:
        if head not in node_map:
            node_map[head] = 1
        else:
            return head

        head = head.next

    return None


def detect_begin(head):
    length = length_cycle(head)
    pointer1, pointer2 = head, head
    count = 0
    while count != length:
        pointer2 = pointer2.next
        count += 1

    length_before_cycle = 1

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        length_before_cycle += 1

    print("Length before cycle = ", length_before_cycle)

    return pointer1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(detect_begin(head).value))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(detect_begin(head).value))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(detect_begin(head).value))
