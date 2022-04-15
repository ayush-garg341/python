"""
Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

example1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

example2:
    Input: head = [2,1], x = 2
    Output: [1,2]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition_list(head, x):

    smaller_head = None
    head1 = None
    larger_head = None
    head2 = None

    while head is not None:
        val = head.val

        if val < x:
            if smaller_head is None:
                smaller_head = head
                head1 = smaller_head
            else:
                smaller_head.next = head
                smaller_head = smaller_head.next
        else:
            if larger_head is None:
                larger_head = head
                head2 = larger_head
            else:
                larger_head.next = head
                larger_head = larger_head.next

        head = head.next

    if smaller_head is not None:
        smaller_head.next = head2
    if larger_head and larger_head.next is not None:
        larger_head.next = None

    if head1 is not None:
        return head1
    return head2


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

new_head = partition_list(head, 3)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next

print("====")
head = ListNode(1)
head.next = ListNode(1)
new_head = partition_list(head, 0)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
