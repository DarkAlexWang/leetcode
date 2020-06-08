#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], maxProd * nums[i], minProd * nums[i])
            y = min(nums[i], maxProd * nums[i], minProd * nums[i])
            maxProd, minProd= x, y
            ans = max(maxProd, ans)
        return ans
# @lc code=end
