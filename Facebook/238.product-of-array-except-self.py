#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_without_self = [1] * n

        for i in range(1, n):
            product_without_self[i] = product_without_self[i -1] * nums[i - 1]

        right_product = 1
        for i in range(n - 1, -1, -1):
            product_without_self[i] = product_without_self[i] * right_product
            right_product = right_product* nums[i]
        return product_without_self
# @lc code=end
