"""
Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum number of
passes required to convert all negative in matrix to positive integers.

Note that 0 is neither pos or negtive so can't convet a negative to positive.
A negative number can only be converted to positive if one or more of its adjacent (left, right, top, bottom) elments is positive.

ex.
[
    [0, -2, -1],
    [-5, 2, 0],
    [-6, -2, 0]
]

output-> 2
first pass -> [
    [0, 2, -1],
    [5, 2, 0],
    [-6, 2, 0]
]


second pass -> [
    [0, 2, 1],
    [5, 2, 0],
    [6, 2, 0]
]

"""


def minimumPassesOfMatrix(matrix):
    # Write your code here.
    # run bfs

    row = len(matrix)
    col = len(matrix[0])
    queue = []

    for i in range(row):
        for j in range(col):
            if matrix[i][j] > 0:
                queue.append((i, j))

    num_pass = 0

    while len(queue):
        size = len(queue)
        while size != 0:
            front = queue.pop(0)
            find_negative_neighbours(front, matrix, queue)
            size -= 1

        num_pass += 1

    for i in range(row):
        for j in range(col):
            if matrix[i][j] < 0:
                return -1

    return num_pass - 1


def find_negative_neighbours(positive_pos, matrix, queue):
    row = positive_pos[0]
    col = positive_pos[1]

    # checking top element
    if row - 1 >= 0:
        if matrix[row - 1][col] < 0:
            queue.append((row - 1, col))
            matrix[row - 1][col] *= -1

    # check lower elements
    if row + 1 < len(matrix):
        if matrix[row + 1][col] < 0:
            queue.append((row + 1, col))
            matrix[row + 1][col] *= -1

    # check previous col element
    if col - 1 >= 0:
        if matrix[row][col - 1] < 0:
            queue.append((row, col - 1))
            matrix[row][col - 1] *= -1

    # check next col element
    if col + 1 < len(matrix[0]):
        if matrix[row][col + 1] < 0:
            queue.append((row, col + 1))
            matrix[row][col + 1] *= -1
