#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return -1, -1

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return -1, -1
        left = l
        l, r = left, len(nums) -1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] == target:
                l = m
            else:
                r = m - 1
        right = l
        return (left, right)

# @lc code=end
