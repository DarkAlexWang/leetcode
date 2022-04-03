#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n is 1:
            return 1
        h, val = [(2, 2), (3, 3), (5, 5)], 1
        for i in range(1, n):
            val, fact = heapq.heappop(h)
            heapq.heappush(h, (val * 5, 5))
            if fact <= 3:
                heapq.heappush(h, (val * 3, 3))
            if fact is 2:
                heapq.heappush(h, (val * 2, 2))
        return val
# @lc code=end
