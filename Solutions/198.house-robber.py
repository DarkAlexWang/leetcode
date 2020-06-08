#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        arry = [0] * len(nums)
        arry[0] = nums[0]
        arry[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            arry[i] = max((arry[i -2] + nums[i], arry[i -1]))
        return arry[len(nums) - 1]
# @lc code=end
