#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        m = {}
        for a in nums1:
            for b in nums2:
                m[a + b] = m.get(a+b, 0) + 1
        for c in nums3:
            for d in nums4:
                cnt += m.get(-(c + d), 0)
        return cnt

# @lc code=end
