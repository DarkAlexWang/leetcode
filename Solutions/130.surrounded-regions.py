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
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = 'G'
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        for x in range(m):
            dfs(x, 0)
            dfs(x, n-1)
        for y in range(n):
            dfs(0, y)
            dfs(m-1, y)
        dic = {'G': 'O', 'O': 'X', 'X': 'X'}
        for x in range(m):
            for y in range(n):
                board[x][y] = dic[board[x][y]]

# @lc code=end
