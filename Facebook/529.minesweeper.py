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
        q = collections.deque([(x, y)])
        visited = set((x, y))
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        def numBombs(board, i, j):
            count = 0
            for dx, dy in dirs:
                row = dx + i
                col = dy + j
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'M':
                    count += 1
            return count
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if board[i][j] == 'E':
                    bombs_next_to = numBombs(board, i, j)
                    board[i][j] = 'B' if bombs_next_to == 0 else str(bombs_next_to)
                    if bombs_next_to == 0:
                        for dx, dy in dirs:
                            row = dx + i
                            col = dy + j
                            if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited:
                                q.append((row, col))
                                visited.add((row, col))
        return board
# @lc code=end
