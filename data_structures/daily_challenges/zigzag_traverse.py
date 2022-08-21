"""
Given nxm 2-d array, return a 1-d array traversed in zig-zag order.

example1
    input:[
          [1, 3, 4, 10],
          [2, 5, 9, 11],
          [6, 8, 12, 15],
          [7, 13, 14, 16]
        ]
    output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""


def zigzag_traverse(array):
    rows = len(array)
    cols = len(array[0])

    result = [array[0][0]]

    if rows == 1 and cols == 1:
        return result

    i = 0
    j = 0
    while True:
        i, j = bottom_to_top(i, j, result, rows, cols, array)
        if i == rows - 1 and j == cols - 1:
            return result
        i, j = top_to_bottom(i, j, result, rows, cols, array)
        if i == rows - 1 and j == cols - 1:
            return result


def bottom_to_top(curr_row, curr_col, result, total_rows, total_cols, array):
    if curr_row < total_rows - 1:
        curr_row += 1
    else:
        curr_col += 1

    while True:
        if curr_row >= 0 and  curr_col < total_cols:
            result.append(array[curr_row][curr_col])
            if curr_row == 0 or curr_col == total_cols - 1:
                return curr_row, curr_col
            curr_row -= 1
            curr_col += 1



def top_to_bottom(curr_row, curr_col, result, total_rows, total_cols, array):
    if curr_col < total_cols - 1:
        curr_col += 1
    else:
        curr_row += 1
    while True:
        if curr_row < total_rows and  curr_col >= 0:
            result.append(array[curr_row][curr_col])
            if curr_row == total_rows - 1 or curr_col == 0:
                return curr_row, curr_col
            curr_row += 1
            curr_col -= 1


inp = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]
print(zigzag_traverse(inp))

def zigzag_traverse_dict(array):
    dic = {}
    result = []

    rows = len(array)
    cols = len(array[0])

    total = rows + cols - 1

    for i in range(rows):
        for j in range(cols):
            if i + j not in dic:
                dic[i+j] = []
            dic[i+j].append(array[i][j])


    for i in range(total):
        if i % 2 == 0:
            result += dic[i]
        else:
            result += reversed(dic[i])

    return result

print(zigzag_traverse_dict(inp))
