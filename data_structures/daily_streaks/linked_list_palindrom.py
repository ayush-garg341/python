class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    # TODO: Write your code here
    is_palin = True
    slow = fast = head
    while True:
        if fast.next is None or fast.next.next is None:
            break
        slow = slow.next
        fast = fast.next.next
        middle = slow
    reversed_list = reverse(middle.next)
    temp = reversed_list
    while reversed_list is not None:
        if reversed_list.value != head.value:
            is_palin = False
            break
        reversed_list = reversed_list.next
        head = head.next

    middle.next = reverse(temp)

    return is_palin

def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

def reverse(head, end_node=None):
    temp = head
    prev = end_node
    while temp != None:
        temp = temp.next
        head.next = prev
        prev = head
        head = temp
    return prev


def is_palindromic_linked_list_extra_space(head):
    nums = []
    while head:
        nums.append(head.value)
        head = head.next

    i = 0
    j = len(nums) - 1
    while i<=j:
        if nums[i] != nums[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(2)
    # head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list_extra_space(head)))

    # print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
