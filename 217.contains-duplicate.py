#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if n in dic: return True
            else: dic[n] = 1
        return False
# @lc code=end
