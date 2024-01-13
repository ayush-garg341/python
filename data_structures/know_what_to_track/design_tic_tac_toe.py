"""
Design tic tac toe. Suppose that two players are playing a tic-tac-toe game on
n x n board.
- A move is guaranteed to be valid if a mark is placed on an empty block.
- No more moves are allowed once a winning condition is reached.
- A player who succeeds in placing n
 of their marks in a horizontal, vertical, or diagonal row wins the game.
"""


class TicTacToe:
    # Constructor will be used to initialize TicTacToe data members
    def __init__(self, n):
        # Write your code here
        self.n = n
        self.tic_tac_toe = [[None for i in range(n)] for j in range(n)]
        self.player_moves = {1: "O", 2: "X"}

    # move will be used to play a move by a specific player and identify who
    # wins at each move
    def move(self, row, col, player):
        # Replace this placeholder return statement with your code
        self.tic_tac_toe[row][col] = self.player_moves[player]
        # check if row contains all player moves

        found = True
        for c in range(self.n):
            if self.tic_tac_toe[row][c] != self.player_moves[player]:
                found = False
                break
        if found:
            return player

        # check if col contains all player moves
        found = True
        for r in range(self.n):
            if self.tic_tac_toe[r][col] != self.player_moves[player]:
                found = False
                break
        if found:
            return player

        # check diagonal
        # diagonal = i == j
        found = True
        for r in range(self.n):
            c = r
            if self.tic_tac_toe[r][c] != self.player_moves[player]:
                found = False
                break
        if found:
            return player

        # anti diagonal j = n - 1 - i
        found = True
        for r in range(self.n):
            c = self.n - 1 - r
            if self.tic_tac_toe[r][c] != self.player_moves[player]:
                found = False
                break
        if found:
            return player

        return 0


class TicTacToeEfficient:
    # Constructor will be used to initialize TicTacToe data members
    def __init__(self, n):
        # Write your code here
        self.n = n
        self.rows = [0 for i in range(n)]
        self.cols = [0 for j in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0
        self.player_moves = {1: 1, 2: -1}

    # move will be used to play a move by a specific player and identify who
    # wins at each move
    def move(self, row, col, player):
        move = self.player_moves[player]
        self.rows[row] += move
        if self.rows[row] == move * self.n:
            return player

        self.cols[col] += move
        if self.cols[col] == move * self.n:
            return player

        if row == col:
            self.diagonal += move

            if self.diagonal == move * self.n:
                return player

        if col == self.n - 1 - row:
            self.antidiagonal += move

            if self.antidiagonal == move * self.n:
                return player

        return 0
