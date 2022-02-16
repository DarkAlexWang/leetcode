#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid, count)
                    count += 1
        return count

    def dfs(self, i, j, grid, count):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(i + 1, j, grid, count)
        self.dfs(i - 1, j, grid, count)
        self.dfs(i, j + 1, grid, count)
        self.dfs(i, j - 1, grid, count)


# @lc code=end
