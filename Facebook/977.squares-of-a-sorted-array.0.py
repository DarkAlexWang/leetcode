#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
import collections
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            left_num, right_num = abs(nums[l]), abs(nums[r])
            if left_num > right_num:
                res.append(left_num * left_num)
                l += 1
            else:
                res.append(right_num * right_num)
                r -= 1
        return res[::-1]

# @lc code=end
