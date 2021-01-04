#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        write_pointer = len(nums) - 1
        l, r = 0, len(nums) - 1
        l_sq = nums[l] ** 2
        r_sq = nums[r] ** 2
        while write_pointer >= 0:
            if l_sq > r_sq:
                res[write_pointer] = l_sq
                l += 1
                l_sq = nums[l] ** 2
            else:
                res[write_pointer] = r_sq
                r -= 1
                r_sq = nums[r] ** 2
            write_pointer -= 1
        return res

# @lc code=end
