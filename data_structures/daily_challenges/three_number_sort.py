"""
Sort numbers in an array according to given order array.

ex:-
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]

    output:- [0, 0, 0, 1, 1, 1, -1, -1]
"""


def threeNumberSortNaive(array, order):
    # Write your code here.
    order_map = {}
    first_elt = order[0]
    second_elt = order[1]
    third_elt = order[2]

    order_map[first_elt] = 0
    order_map[second_elt] = 0
    order_map[third_elt] = 0

    n = len(array)
    for i in range(n):
        order_map[array[i]] += 1

    size = 0
    for i in range(order_map[first_elt]):
        array[size] = first_elt
        size += 1

    for i in range(order_map[second_elt]):
        array[size] = second_elt
        size += 1

    for i in range(order_map[third_elt]):
        array[size] = third_elt
        size += 1

    return array


print(threeNumberSortNaive([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))


def threeNumberSortTwoPass(array, order):
    first = order[0]
    third = order[2]

    # first pass, position first ordered element
    start = i = 0
    n = len(array) - 1
    while start <= n:
        if array[start] == first:
            if start != i:
                array[start], array[i] = array[i], array[start]
            start += 1
            i += 1
        else:
            start += 1

    # second pass, position the last element
    end = j = n
    while end >= 0:
        if array[end] == third:
            if end != j:
                array[end], array[j] = array[j], array[end]
            end -= 1
            j -= 1
        else:
            end -= 1

    return array


print(threeNumberSortTwoPass([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))


def threeNumberSortSinglePass(array, order):
    """
    Similary to Dutch national flag problem.
    Approach:- Iterate over the array, if at any pos we find first element, we swap it with leftmost non-first pos.
        If we find second element we continue as is, since second element must be in middle.
        If we find third element then we swap it with last non-third pos
    """
    first, second, third = order[0], order[1], order[2]

    i = 0
    j = 0
    k = len(array) - 1

    while j <= k:
        if array[j] == first:
            array[i], array[j] = array[j], array[i]
            j += 1
            i += 1
        elif array[j] == third:
            array[j], array[k] = array[k], array[j]
            k -= 1
        else:
            j += 1

    return array


print(threeNumberSortSinglePass([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
