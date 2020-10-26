#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return res
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, index, res):
        if index == len(nums):
            res.append(nums.copy())
            return

        used = {}
        for i in range(index, len(nums)):
            if nums[i] not in used:
                used[nums[i]] =  1
                self.swap(nums, i, index)
                self.dfs(nums, index+ 1, res)
                self.swap(nums, i, index)

    def swap(self, arry, left, right):
        tmp = arry[left]
        arry[left] = arry[right]
        arry[right] = tmp

# @lc code=end
