#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#

# @lc code=start
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.dirs = [(0,-1), (-1, 0), (0, 1), (1, 0)]
        m, n = len(grid), len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                v = []
                self.helper(grid, i, j, i, j, v)
                res.add(tuple(v))
        return len(res)
    def helper(self, grid, x0, y0, i, j, v):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] <= 0:
            return
        grid[i][j] *= -1
        v.append((i - x0, j - y0))
        for d in self.dirs:
            self.helper(grid, x0, y0, i + d[0], j + d[1], v)


# @lc code=end
