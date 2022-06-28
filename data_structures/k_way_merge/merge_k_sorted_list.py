"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

example1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
    Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

example2:
    Input: L1=[5, 8, 9], L2=[1, 7]
    Output: [1, 5, 7, 8, 9]
"""

import heapq


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    resultHead = head = None
    min_heap = []
    for root in lists:
        if root is not None:
            heapq.heappush(min_heap, root)

    while len(min_heap):
        min_elt = heapq.heappop(min_heap)
        if resultHead is None:
            resultHead = head = min_elt
        else:
            resultHead.next = min_elt
            resultHead = resultHead.next
        if min_elt.next is not None:
            heapq.heappush(min_heap, min_elt.next)

    return head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end="")
    while result != None:
        print(str(result.value) + " ", end="")
        result = result.next


main()
