"""
Sorting using priority queue.
We can sort in-place using maximum binary heap.
"""


def pq_sort(C):
    """
    Sort a collection of elements stored in a positional list C.
    """
    n = len(C)
    p = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        p.add(element, element)
    for j in range(n):
        (k, v) = p.remove_min()
        C.add_last(v)
