"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
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

def reverse_sub_list(head, p, q):
    if p > q:
        return head
    front = 1
    front_head = head
    while front < p-1:
        front_head = front_head.next
        front += 1

    temp_head = front_head
    end = 1
    last_head = head
    while end < q:
        last_head = last_head.next
        end += 1

    temp_last = last_head.next

    last_head.next = None

    if p == 1:
        front_head = head
    else:
        front_head = front_head.next

    reversed_list_head = reverse_list(front_head)
    temp = front_head
    temp.next = temp_last
    if p == 1:
        head = reversed_list_head
    else:
        temp_head.next = reversed_list_head

    return head

def reverse_list(head):
    prev = None
    temp = head
    while temp is not None:
        temp = temp.next
        head.next = prev
        prev = head
        head = temp
    return prev

# def main():
    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)

    # print("Nodes of original LinkedList are: ", end='')
    # head.print_list()
    # result = reverse_sub_list(head, 1, 5)
    # print("Nodes of reversed LinkedList are: ", end='')
    # result.print_list()
# main()

def reverse_every_k_elements(head, k):
    length = 0
    temp = head
    while temp is not None:
        temp = temp.next
        length += 1
    count = 0
    k_group = 0
    count_group = 0
    while count < length:
        count += 1
        if count % k == 0:
            k_group = k*count_group + 1
            count_group += 1
            head = reverse_sub_list(head, k_group, count)

    if count % k != 0:
        rem = count % k
        head = reverse_sub_list(head, count - rem + 1, count)

    return head


def main2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main2()
