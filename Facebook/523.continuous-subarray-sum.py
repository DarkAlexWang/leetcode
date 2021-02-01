#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            sum_arr = nums[i]
            for j in range(i + 1, len(nums)):
                sum_arr += nums[j]
                if sum_arr == k:
                    return True
                if k != 0 and sum_arr % k == 0:
                    return True
        return False
# @lc code=end
