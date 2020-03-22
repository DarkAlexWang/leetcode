#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (29.53%)
# Total Accepted:    159.1K
# Total Submissions: 538.9K
# Testcase Example:  '[2,3,1,1,4]'
#
# 
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# 
# Each element in the array represents your maximum jump length at that
# position. 
# 
# 
# Determine if you are able to reach the last index.
# 
# 
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# 
# A = [3,2,1,0,4], return false.
# 
#
class Solution(object):
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
        
