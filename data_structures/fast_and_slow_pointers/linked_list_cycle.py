"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    if head is None or head.next is None:
        return False
    slow = head.next
    fast = head.next.next
    while slow is not None:
        if slow != fast:
            slow = slow.next
            if fast is not None and fast.next is not None:
                fast = fast.next.next
            else:
                return False
        else:
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next


print(has_cycle(head))


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

print(has_cycle(head))
