#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start
class TicTacToe:

    def __init__(self, n: int):
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        move = 1
        if player == 2:
            move = -1

        self.row[row] += move
        self.col[col] += move

        if row == col:
            self.diag += move

        if row + col == (n - 1):
            self.anti_diag += move

        if abs(self.col[col]) == n or abs(self.row[row]) == n \
                or abs(self.diag) == n or abs(self.anti_diag) == n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# @lc code=end
