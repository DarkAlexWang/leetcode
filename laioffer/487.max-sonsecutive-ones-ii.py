#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 1
        slow = 0
        ans = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                k -= 1
            if k < 0:
                if nums[slow] == 0:
                    k += 1
                slow += 1
            ans = max(ans, fast - slow + 1)
        return ans

# @lc code=end
