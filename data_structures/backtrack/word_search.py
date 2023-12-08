"""

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        is_exist = False
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                visited = set()
                is_exist = self.search_word_rec(board, word, visited, i, j, 0)
                if is_exist:
                    return True
        return False

    def search_word_rec(
        self, board, word, visited, current_row, current_col, current_idx
    ):
        if current_idx == len(word):
            return True
        if (current_row, current_col) in visited:
            return False
        if (
            current_row < 0
            or current_row >= len(board)
            or current_col < 0
            or current_col >= len(board[0])
            or board[current_row][current_col] != word[current_idx]
        ):
            return False

        visited.add((current_row, current_col))

        ret = self.search_word_rec(
            board, word, visited, current_row, current_col + 1, current_idx + 1
        )
        if ret:
            return ret
        ret = self.search_word_rec(
            board, word, visited, current_row, current_col - 1, current_idx + 1
        )
        if ret:
            return ret
        ret = self.search_word_rec(
            board, word, visited, current_row + 1, current_col, current_idx + 1
        )
        if ret:
            return ret
        ret = self.search_word_rec(
            board, word, visited, current_row - 1, current_col, current_idx + 1
        )
        if ret:
            return ret

        visited.remove((current_row, current_col))
        return False


soln = Solution()
# print(
# soln.exist(
# [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
# )
# )

# print(
# soln.exist(
# [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
# )
# )

# print(
# soln.exist(
# [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
# )
# )

# print(soln.exist([["a", "b"], ["c", "d"]], "acdb"))
print(soln.exist([["a", "a", "a"], ["A", "A", "A"], ["a", "a", "a"]], "aAaaaAaaA"))
