"""
Find the middle node of a linked list and return it.

example1:
    Input:  1->2->3
    Output: 2
    Explanation: return the middle node.

example2:
    Input:  1->2
    Output: 1
    Explanation: If the length of list is even return the center left one.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def left_middle_of_list(head):
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


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Middle Node: " + str(left_middle_of_list(head).value))

head.next.next.next.next.next = Node(6)
print("Middle Node: " + str(left_middle_of_list(head).value))

head.next.next.next.next.next.next = Node(7)
print("Middle Node: " + str(left_middle_of_list(head).value))
