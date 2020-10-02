#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res *26 + ord(i) - ord('A') + 1
        return res
# @lc code=end
