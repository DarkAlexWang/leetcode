#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex +1):
            for j in range(i, 0, -1):
                res[j] += res[j -1]
        return res
# @lc code=end
