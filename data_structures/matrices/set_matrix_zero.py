"""
Given a matrix, mat, if any element within the matrix is zero,
set that row and column to zero.
"""


def set_matrix_zero(mat):
    rows = len(mat)
    cols = len(mat[0])
    vset = set()
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 0 and (row, col) not in vset:
                vset.add((row, col))
                mark_as_zero(row, col, mat, vset)
    return mat


def mark_as_zero(row, col, mat, vset):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        mat[i][col] = 0
        vset.add((i, col))
    for j in range(cols):
        mat[row][j] = 0
        vset.add((row, j))


print(set_matrix_zero([[1, 2, 3], [4, 5, 6], [7, 0, 9]]))
