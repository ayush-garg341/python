"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

example1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]

example2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0, 1, 1, 4, 9]
"""


def square_sorted_array(arr):
    start = 0
    end = len(arr) - 1
    squares = [None for i in range(len(arr))]
    sq_ind = end

    while start <= end:
        sq_start = arr[start] * arr[start]
        sq_end = arr[end] * arr[end]

        if sq_end > sq_start:
            squares[sq_ind] = sq_end
            end -= 1
            sq_ind -= 1
        elif sq_end < sq_start:
            squares[sq_ind] = sq_start
            start += 1
            sq_ind -= 1
        else:
            squares[sq_ind] = sq_end
            sq_ind -= 1
            end -= 1

    return squares


print(square_sorted_array([-2, -1, 0, 2, 3]))
print(square_sorted_array([-3, -1, 0, 1, 2]))


def square_sorted_array_another_approach(arr):
    index_pos_num = -1
    for i in range(len(arr)):
        if arr[i] >= 0:
            index_pos_num = i
            break

    if index_pos_num == 0:
        return [arr[i] * arr[i] for i in range(len(arr))]
    if index_pos_num == -1:
        return [arr[i]*arr[i] for i in range(len(arr)-1, -1, -1)]

    negative_num_index = index_pos_num - 1
    squares = []
    while negative_num_index >= 0 and index_pos_num <= len(arr) - 1:
        neg_sq = arr[negative_num_index] * arr[negative_num_index]
        pos_sq = arr[index_pos_num] * arr[index_pos_num]

        if pos_sq < neg_sq:
            squares.append(pos_sq)
            index_pos_num += 1
        else:
            squares.append(neg_sq)
            negative_num_index -= 1

    while negative_num_index >= 0:
        squares.append(arr[negative_num_index]*arr[negative_num_index])
        negative_num_index -= 1

    while index_pos_num <= len(arr) - 1:
        squares.append(arr[index_pos_num]*arr[index_pos_num])
        index_pos_num += 1

    return squares


print(square_sorted_array_another_approach([-2, -1, 0, 2, 3]))
print(square_sorted_array_another_approach([-3, -1, 0, 1, 2]))










