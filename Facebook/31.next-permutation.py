#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
# [1, 2, 7, 4, 3, 1]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_small = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i]< nums[i + 1]:
                first_small = i
                break

        if first_small == -1:
            nums = nums[::-1].copy()
            print('nums1:',  nums)
            return nums

        else:
            first_large = -1
            for i in range(len(nums) -1, first_small, -1):
                if nums[i] > nums[first_small]:
                    first_large = i
                    break
            nums[first_small], nums[first_large] = nums[first_large], nums[first_small]
            print('nums:2 ', nums)
            print(first_large)

            i, j = first_small + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j]  = nums[j], nums[i]
                i += 1
                j -= 1
        return
# @lc code=end
