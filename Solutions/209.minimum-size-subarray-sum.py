#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 0
        minlength = len(nums) + 1
        res = 0
        while r < len(nums):
            res += nums[r]
            r += 1

            while res >= s:
                minlength = min(minlength, r -l)
                res -= nums[l]
                l += 1
                print(res)
        return 0 if minlength == len(nums) + 1 else minlength
# @lc code=end
