#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        start, end = 0, x -1
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            else:

                if (mid + 1) * (mid + 1) > x:
                    return mid
                start = mid + 1

# @lc code=end
