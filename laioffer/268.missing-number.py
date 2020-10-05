#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in nums_set:
                return i
# @lc code=end
