#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc code=start
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        res = 0
        n = len(ages)
        ages.sort()
        for i in range(n):
            a = ages[i]
            if a <= 14:
                continue
            idx1 = bisect.bisect(ages, a)
            x = 0.5 * a + 7
            idx2 = bisect.bisect(ages, x)
            while idx2 < n and ages[idx2] == x:
                idx2 += 1
            res += max(0, idx1 - idx2 + (-1 if idx2 <= i <= idx1 else 0))
        return res
# @lc code=end
