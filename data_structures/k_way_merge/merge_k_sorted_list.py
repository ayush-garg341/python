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
    """
    Time complexity = O(N*log(k))
    N - total number of elements in all lists
    k - number of lists
    """
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


def merge_lists_by_combining(lists):
    """
    Time complexity = O(N*k)
    N - number of elements in each list
    k - number of lists
    """
    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    temp_list = lists[0]
    for i in range(1, len(lists)):
        temp_list = merge(temp_list, lists[i])

    return temp_list


def merge(temp_list, to_be_merged):
    temp = None
    main_head = None
    temp_head = temp_list
    to_be_merged_head = to_be_merged
    while temp_head is not None and to_be_merged_head is not None:
        if temp_head.value > to_be_merged_head.value:
            if temp is None:
                temp = main_head = to_be_merged_head
            else:
                temp.next = to_be_merged_head
                temp = temp.next
            to_be_merged_head = to_be_merged_head.next
        else:
            if temp is None:
                temp = main_head = temp_head
            else:
                temp.next = temp_head
                temp = temp.next
            temp_head = temp_head.next

    if temp_head is not None:
        if temp is None:
            temp = main_head = temp_head
        else:
            temp.next = temp_head

    if to_be_merged_head is not None:
        if temp is None:
            temp = main_head = to_be_merged
        else:
            temp.next = to_be_merged_head

    return main_head


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

    # result = merge_lists([l1, l2, l3])
    result = merge_lists_by_combining([l1, l2, l3])
    print("Here are the elements form the merged list: ", end="")
    while result != None:
        print(str(result.value) + " ", end="")
        result = result.next


main()
