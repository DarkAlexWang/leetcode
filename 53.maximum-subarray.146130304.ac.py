#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (40.21%)
# Total Accepted:    285K
# Total Submissions: 708.8K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        
        prev = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            res = max(res, prev)
        return res
