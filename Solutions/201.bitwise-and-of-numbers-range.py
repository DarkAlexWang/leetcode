#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        d = sys.maxsize
        while m & d != n &d:
            d <<= 1
        return m & d
# @lc code=end
