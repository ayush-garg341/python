    # TODO: Write your code here
    slow = fast = head
    middle = slow
    main_head = head
    while True:
        if fast.next is None or fast.next.next is None:
            middle = slow
            break
        slow = slow.next
        fast = fast.next.next

    second_half_reversed = reverse(middle.next)
    middle.next = None
    while second_half_reversed is not None:
        temp = head.next
        head.next = second_half_reversed
        temp_reversed = second_half_reversed.next
        head.next.next = temp
        head = temp
        second_half_reversed = temp_reversed

    return main_head


def reverse(head):
    temp = head
    prev = None
    while temp != None:
        temp = temp.next
        head.next = prev
        prev = head
        head = temp
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()

