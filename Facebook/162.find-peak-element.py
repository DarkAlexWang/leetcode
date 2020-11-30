#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        #while l < r:
        #    mid = (l + r) // 2
        #    if nums[mid] > nums[mid + 1]:
        #        r = mid
        #    else:
        #        l = mid + 1
        #return l
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid -1]:
                return mid
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid
        if nums[l] < nums[r]:
            return r
        else:
            return l
# @lc code=end
