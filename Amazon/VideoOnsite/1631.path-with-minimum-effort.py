#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        rows = len(heights)
        cols = len(heights[0])
        pq = [(0, 0, 0)]
        seen = set()
        while pq:
            cost, r, c = heapq.heappop(pq)
            if (r, c) in seen:
                continue
            seen.add((r, c))

            if (r, c) == (rows - 1, cols - 1):
                return cost
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = dr + r, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(pq, (max(cost, abs(heights[nr][nc] - heights[r][c])), nr, nc))

# @lc code=end
