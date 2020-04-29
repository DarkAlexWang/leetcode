#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        lastpos = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0
# @lc code=end
