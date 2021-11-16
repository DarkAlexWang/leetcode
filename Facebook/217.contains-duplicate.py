#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = collections.defaultdict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] >= 2:
                return True

        return False
# @lc code=end
