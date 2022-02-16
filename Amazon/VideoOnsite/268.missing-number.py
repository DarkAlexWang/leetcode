#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0 for _ in range(n + 1)]
        for idx, value in enumerate(nums):
            res[value] = 1
        for idx, value in enumerate(res):
            if value == 0:
                return idx



# @lc code=end
