# @lc lang=python3
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n - 1 and j == n - 1:
                return d
            dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in dirs:
                dx = i + x
                dy = j + y
                if 0 <= dx < n and 0 <= dy < n and not grid[dx][dy]:
                    grid[dx][dy] = 1
                    q.append((dx, dy, d + 1))
        return -1
