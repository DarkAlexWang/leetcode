#
# @lc app=leetcode id=1730 lang=python3
#
# [1730] Shortest Path to Get Food
#

# @lc code=start
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        q = collections.deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i, j, 0))
                    break
        while q:
            i, j, steps = q.popleft()
            for x, y in dirs:
                n_i = x + i
                n_j = y + j
                if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] in ('#', 'O'):
                    if grid[n_i][n_j] == '#':
                        return steps + 1
                    grid[n_i][n_j] = '!'
                    q.append((n_i, n_j, steps + 1))
        return -1

# @lc code=end
