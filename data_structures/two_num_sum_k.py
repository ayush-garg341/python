def find_sum(lst, k):
    s = set()
    for num in lst:
        s.add(num)

    for num in lst:
        num2 = k - num
        if num2 in s and num != num2:
            return [num, num2]


print(find_sum([3, 1, 21, 3, 14, 5, 60, 7, 6], 6))


def find_sum_moving_indices(lst, k):
    lst.sort()
    i = 0
    j = len(lst) - 1

    while i < j:
        if lst[i] + lst[j] == k:
            return [lst[i], lst[j]]
        elif lst[i] + lst[j] > k:
            j -= 1
        else:
            i += 1


print(find_sum_moving_indices([1, 21, 3, 14, 5, 60, 7, 6], 6))
