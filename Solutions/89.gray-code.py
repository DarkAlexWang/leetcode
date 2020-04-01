#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            size = len(res)
            for k in range(size-1,-1,-1):
                res.append(res[k] | 1<<i)
        return res
# @lc code=end
