"""
Given the head of a LinkedList with a cycle, find the length of the cycle.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def length_cycle_naive(head):
    node_map = {}
    count = 1
    while head is not None:
        if head not in node_map:
            node_map[head] = count
            count += 1
        else:
            return count - node_map[head]

        head = head.next


def length_cycle(head):
    meeting_node = find_meet_node(head)
    if meeting_node is None:
        return -1
    length = 1
    temp = meeting_node
    while meeting_node.next != temp:
        length += 1
        meeting_node = meeting_node.next

    return length


def find_meet_node(head):
    if head is None or head.next is None:
        return None
    slow = head.next
    fast = head.next.next
    while slow is not None:
        if slow != fast:
            slow = slow.next
            if fast is not None and fast.next is not None:
                fast = fast.next.next
            else:
                return None
        else:
            return slow
    return None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next


print(length_cycle_naive(head))
print(length_cycle(head))

head.next.next.next.next.next.next = head.next.next.next
print(length_cycle_naive(head))
print(length_cycle(head))
