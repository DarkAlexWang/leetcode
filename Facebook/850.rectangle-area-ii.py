#
# @lc app=leetcode id=850 lang=python3
#
# [850] Rectangle Area II
#

# @lc code=start
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        ys = sorted(set([y for x1, y1, x2, y2 in rectangles for y in [y1, y2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        y_i = {v: i for i, v in enumerate(ys)}
        m, n = len(y_i), len(x_i)

        grid = [[0] * m for _ in range(n)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(x_i[x1], x_i[x2]):
                for y in range(y_i[y1], y_i[y2]):
                    grid[x][y] = 1
        ans = 0
        for x in range(n- 1):
            for y in range(m - 1):
                ans += grid[x][y] * (xs[x + 1] - xs[x]) * (ys[y + 1] - ys[y])
        return ans % (10 ** 9 + 7)

# @lc code=end
