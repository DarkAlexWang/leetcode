#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        wordDict = set(wordDict)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

# @lc code=end
