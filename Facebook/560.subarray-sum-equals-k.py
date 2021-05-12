#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        hash_table = collections.defaultdict(lambda:0)
        total = 0
        for x in nums:
            running_sum += x
            sum_ = running_sum - k
            if sum_ in hash_table:
                total += hash_table[sum_]
            if running_sum == k:
                total += 1
            hash_table[running_sum] += 1
        return total

# @lc code=end
