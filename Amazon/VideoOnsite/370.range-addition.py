#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#

# @lc code=start
class Solution:
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for start, end, value in updates:
            res[start] += value
            end += 1
            if end < len(res):
                res[end] -= value
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res
# @lc code=end
