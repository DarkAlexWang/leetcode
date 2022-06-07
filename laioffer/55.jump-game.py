#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp = [False] * len(nums)
        #dp[0] = True
        #for i in range(1, len(nums)):
        #    for j in range(i):
        #        if dp[j] and nums[j] >= i - j:
        #            dp[i] = True
        #            break
        #return dp[-1]
        last_position = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0
# @lc code=end
