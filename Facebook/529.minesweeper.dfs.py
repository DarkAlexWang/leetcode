#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        self.dfs(board, x, y)
        return board

    def dfs(self, board, i, j):

        if board[i][j] != 'E':
            continue

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

        count = 0
        for dx, dy in dirs:
            row = dx + i
            col = dy + j
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'M':
                count += 1
        if count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(count)
            return

        for dx, dy in dirs:
            row = dx + i
            col = dy + j
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                self.dfs(board, row, col)

        return board
# @lc code=end
