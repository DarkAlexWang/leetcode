#
# @lc app=leetcode id=1062 lang=python3
#
# [1062] Longest Repeating Substring
#

# @lc code=start
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if s[i -1] == s[j - 1] else 0
                res = max(res, dp[i][j])
        return res
# @lc code=end
