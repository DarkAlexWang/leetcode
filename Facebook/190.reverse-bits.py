#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out
# @lc code=end
