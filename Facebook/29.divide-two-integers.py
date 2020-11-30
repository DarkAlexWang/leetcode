#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
import sys
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) == (divisor > 0)
        res = 0
        x,y = abs(dividend), abs(divisor)
        while x >= y:
            temp, i = y, 1
            while x >= temp:
                x -= temp
                temp <<= 1
                res += i
                i <<= 1

        if not positive:
            res = -1 * res
        return min(max(res, -2147483648), 2147483647)


# @lc code=end
