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
        left, right = -1, -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            left = l
        else:
            return -1, -1
        l, r = left, len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if nums[mid] == target:
                l = mid
            else:
                r = mid - 1
        right = l
        return left, right
# @lc code=end
