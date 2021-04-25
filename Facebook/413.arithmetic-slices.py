#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
import sys
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res, diff, count, start = 0, -sys.maxsize, 0, 0
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            if curr_diff == diff:
                count += i - start - 1 if i - start - 1 > 0 else 0
            else:
                start = i - 1
                diff = curr_diff
                res += count
                count = 0
        res += count
        return res

# @lc code=end
