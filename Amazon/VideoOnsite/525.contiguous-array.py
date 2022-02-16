#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length= 0
        dic = {}
        count = 0
        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                count -= 1
            else:
                count += 1
            if count == 0:
                max_length = i + 1
            if count in dic:
                max_length = max(max_length, i - dic[count])
            else:
                dic[count] = i
        return max_length

# @lc code=end
