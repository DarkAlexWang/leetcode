#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k

# @lc code=end
