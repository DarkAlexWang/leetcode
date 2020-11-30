#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)  // 2
            if mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                l = mid + 1
            elif mid % 2 == 1 and nums[mid] == nums[mid -1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


# @lc code=end
