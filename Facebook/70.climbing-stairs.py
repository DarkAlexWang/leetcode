#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step_before = 2
        two_steps_before = 1
        all_ways = 0
        for i in range(2, n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways
        return all_ways
# @lc code=end
