#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        counts =  {0: 1}
        sumValue, ans = 0, 0
        for num in nums:
            sumValue += num
            ans += counts[sumValue - k]
            counts[sumValue] += 1
        return ans
# @lc code=end
