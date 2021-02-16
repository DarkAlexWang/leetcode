#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_table = {}
        total = 0
        max_len = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in sum_table:
                sum_table[total] = i
            remain = total - k
            if remain == 0:
                max_len = max(i +1, max_len)
            elif remain in sum_table:
                max_len = max(i - sum_table[remain], max_len)
        return max_len
# @lc code=end
