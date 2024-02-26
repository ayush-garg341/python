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


def set_matrix_zero_optimized(mat):
    rows = len(mat)
    cols = len(mat[0])
    frow = False
    fcol = False
    for i in range(cols):
        if mat[0][i] == 0:
            frow = True

    for j in range(rows):
        if mat[j][0] == 0:
            fcol = True

    for row in range(1, rows):
        for col in range(1, cols):
            if mat[row][col] == 0:
                mat[row][0] = mat[0][col] = 0

    for row in range(1, rows):
        if mat[row][0] == 0:
            for col in range(1, cols):
                mat[row][col] = 0

    for col in range(1, cols):
        if mat[0][col] == 0:
            for row in range(1, rows):
                mat[row][col] = 0

    if frow:
        for col in range(cols):
            mat[0][col] = 0

    if fcol:
        for row in range(rows):
            mat[row][0] = 0
