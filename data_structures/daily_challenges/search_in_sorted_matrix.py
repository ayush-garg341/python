def searchInSortedMatrix(matrix, target):
    # Write your code here.
    m = len(matrix)
    n = len(matrix[0])

    row = 0
    col = n - 1
    while row >= 0 and row < m and col >= 0 and col < n:
        current_val = matrix[row][col]
        if current_val == target:
            return [row, col]
        elif target > current_val:
            row += 1
        else:
            col -= 1
    return [-1, -1]


print(
    searchInSortedMatrix(
        [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ],
        44,
    )
)
