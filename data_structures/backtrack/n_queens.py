"""
Given a chessboard of size nxn, determine how many ways n
 queens can be placed on the board, such that no two queens attack each other.
"""


def is_valid_move(proposed_col, proposed_row, solution):
    for i in range(proposed_row):
        old_row = i
        old_col = solution[i]
        diagonal_offset = proposed_row - old_row
        if (
            old_col == proposed_col
            or old_col == proposed_col - diagonal_offset
            or old_col == proposed_col + diagonal_offset
        ):
            return False

    return True


def solve_n_queens_rec(n, solution, row, results):
    if row == n:
        results.append(solution[:])
        return

    for i in range(n):
        if is_valid_move(i, row, solution):
            solution[row] = i
            solve_n_queens_rec(n, solution, row + 1, results)


def solve_n_queens(n):
    results = []
    solution = [-1] * n
    solve_n_queens_rec(n, solution, 0, results)
    return len(results)


print(solve_n_queens(4))
print(solve_n_queens(5))
