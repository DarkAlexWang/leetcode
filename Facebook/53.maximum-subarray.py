#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        max_num = -sys.maxsize
        for i in range(len(nums)):
            cur += nums[i]
            max_num = max(max_num, cur)
            if cur < 0:
                cur = 0
        return max_num
# @lc code=end
