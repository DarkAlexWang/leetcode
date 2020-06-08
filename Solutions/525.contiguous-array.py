#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        maxLenth = 0
        table = {0 : 0}
        for i, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in table:
                maxLenth = max(maxLenth, i - table[count])
            else:
                table[count] = i
        return maxLenth
# @lc code=end
