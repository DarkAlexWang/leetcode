#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])


        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or board[y][x] != 'O':
                return
            board[y][x] = 'G'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for y in range(m):
            dfs(0, y)
            dfs(n - 1, y)
        for x in range(n):
            dfs(x, 0)
            dfs(x, m -1)
        dic = {'G' :'O', 'O' : 'X','X' : 'X'}
        for y in range(m):
            for x in range(n):
                board[y][x] = dic[board[y][x]]

# @lc code=end
