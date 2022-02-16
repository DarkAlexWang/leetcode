#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        q = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    q.append((i, j))
                    self.bfs(grid, q)
                    count += 1
        return count
    def bfs(self, grid, q):
        while q:
            dx, dy = q.popleft()
            for i, j in [[dx + 1, dy], [dx - 1, dy], [dx, dy + 1], [dx, dy -1]]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    q.append((i, j))
                    grid[i][j] = '0'


# @lc code=end
