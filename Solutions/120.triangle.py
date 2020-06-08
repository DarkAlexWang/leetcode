#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        minlen = [0] * (n + 1)
        for layer in range(n - 1, -1, -1):
            for i in range(layer + 1):
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]
                print(minlen)
        return minlen[0]
#
#
# @lc code=end
