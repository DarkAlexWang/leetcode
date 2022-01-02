#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1
        res += min(prev, cur)
        return res
# @lc code=end
