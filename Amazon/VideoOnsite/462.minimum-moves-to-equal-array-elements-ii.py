#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums)//2]
        return sum(abs(num - median) for num in nums)

# @lc code=end
