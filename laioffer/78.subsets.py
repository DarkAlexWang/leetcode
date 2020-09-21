#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
    def dfs(self, nums, index, path, ans):
        if index == len(nums):
            ans.append(path.copy())
            return
        self.dfs(nums, index +1, path, ans)
        path.append(nums[index])
        print(path)
        self.dfs(nums, index +1, path, ans)
        path.pop()
# @lc code=end
