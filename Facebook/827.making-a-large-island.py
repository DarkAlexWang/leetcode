#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def move(x, y):
            for i, j in ((1,0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < n and 0 <= y + j < n:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        index = 2
        areas = {0 : 0}
        for x in range(n):
            for y in range(n):
                if grid[x][y] ==  1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        res = max(areas.values())
        for x in range(n):
            for j in range(n):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res
# @lc code=end
