#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == 1:
                fast += 1
                res = max(res, fast - slow)
            else:
                fast += 1
                slow = fast
        return res
# @lc code=end
