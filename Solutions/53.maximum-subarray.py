#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)  == 0:
            return
        n = len(nums)
        dp = [-sys.maxsize] * n
        dp[0] = nums[0]
        globalmax = dp[0]
        for i in range(1, n):
            dp[i] = nums[i]  + (dp[i - 1] if dp[i -1] > 0 else 0)
            globalmax = max(globalmax, dp[i])
        return globalmax
# @lc code=end
