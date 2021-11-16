#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:

        c = 0
        while n:
            n &= (n - 1)
            c += 1
        return c

        #return bin(n).count('1')
# @lc code=end
