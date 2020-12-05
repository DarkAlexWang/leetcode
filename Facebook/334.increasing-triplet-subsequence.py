#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min1, min2 = sys.maxsize, sys.maxsize
        for i in range(len(nums)):
            if nums[i] > min2:
                return True
            if nums[i] < min1:
                min1 = nums[i]
            elif min1 < nums[i] < min2:
                min2 = nums[i]
        return False

# @lc code=end
