#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(piles, speed):
            return sum((pile - 1)//speed + 1 for pile in piles) <= H
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if feasible(piles, mid):
                r = mid
            else:
                l = mid + 1
        return l
# @lc code=end
