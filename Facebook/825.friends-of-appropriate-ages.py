#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc code=start
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        n = len(ages)
        ages.sort()
        for i in range(n - 1, 0, -1):
            for j in range(i -1, -1, -1):
                if ages[j] <= 0.5* ages[i] + 7:
                    continue
                if ages[i] == ages [j]:
                    res += 1
                res += 1
        return res
# @lc code=end
