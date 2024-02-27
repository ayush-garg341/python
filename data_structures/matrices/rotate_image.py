"""
Given an nxn matrix, rotate it clockwise by 90 degrees

Algo:-
- Traverse group of four cells, starting from four corners
- Swap the top-left cell with top-right cell
- Swap the top-left cell with bottom-right cell
- Swap the top-left cell with bottom-left cell
- Move to the next group of four cells
"""


def rotate_image(matrix):
    n = len(matrix)
    for row in range(n // 2):
        for col in range(row, n - row - 1):
            matrix[row][col], matrix[col][n - 1 - row] = (
                matrix[col][n - 1 - row],
                matrix[row][col],
            )
            matrix[row][col], matrix[n - 1 - row][n - 1 - col] = (
                matrix[n - 1 - row][n - 1 - col],
                matrix[row][col],
            )
            matrix[row][col], matrix[n - 1 - col][row] = (
                matrix[n - 1 - col][row],
                matrix[row][col],
            )
    return matrix


print(rotate_image([[6, 9], [2, 7]]))
print(rotate_image([[2, 14, 8], [12, 7, 14], [3, 3, 7]]))
