#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n, right_max = len(T), float('-inf')
        res = [0] * n

        for i in range(n - 1, -1, -1):
            if right_max <= T[i]:
                right_max = T[i]
            else:
                days = 1
                while T[i] >= T[i + days]:
                    days += res[i + days]
                res[i] = days
        return res
# @lc code=end
