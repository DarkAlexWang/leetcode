#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        left = 0
        right = left + 1
        while right <= len(nums) - 1:
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                self.swap(nums, left, right)
                left += 1
                right += 1

    def swap(self, array, left, right):
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
# @lc code=end
