#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                k -= 1
            if k < 0:
                if nums[slow] == 0:
                    k += 1
                slow += 1
        return fast - slow + 1
# @lc code=end
