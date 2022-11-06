"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

def word_search(grid, word):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            visited = [[0 for i in range(n)] for j in range(m)]
            ret = visit_adjacent_cells(grid, visited, i, j, m, n, word, 0)
            # print(ret, i, j)
            if ret:
                return True
            # break
        # break

    return False



def visit_adjacent_cells(board, visited, current_row, current_column, total_rows, total_columns, word, idx):
    if idx >= len(word):
        return True

    if current_row < 0 or current_row >= total_rows or current_column >= total_columns or current_column < 0:
        return False

    # if current_row < total_rows and current_column < total_columns:
    if not visited[current_row][current_column] and board[current_row][current_column] == word[idx]:
        # print(current_row, current_column, idx)
        visited[current_row][current_column] = 1
        ret = visit_adjacent_cells(board, visited, current_row, current_column+1, total_rows, total_columns, word, idx + 1)
        if ret:
            return True
        ret = visit_adjacent_cells(board, visited, current_row + 1, current_column, total_rows, total_columns, word, idx + 1)
        if ret:
            return True
        ret = visit_adjacent_cells(board, visited, current_row, current_column-1, total_rows, total_columns, word, idx + 1)
        if ret:
            return True
        ret = visit_adjacent_cells(board, visited, current_row-1, current_column, total_rows, total_columns, word, idx + 1)
        if ret:
            return True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(word_search(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(word_search(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "ADEE"

print(word_search(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCESEEDAS"
print(word_search(board, word))

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(word_search(board, word))
