#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            summ = summ + n
            t = summ if k == 0 else summ % k
            if t not in dic:
                dic[t] = i
            else:
                if i - dic[t] >= 2:
                    return True
        return False
# @lc code=end
