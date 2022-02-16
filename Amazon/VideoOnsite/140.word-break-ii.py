#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return [""]

        self.res = []
        self.wordDict = set(wordDict)
        self.dp = self.isWordBreak(s, wordDict)
        self.backtrack(s, 0, [])

        return self.res

    def backtrack(self, s, idx, path):
        if self.dp[idx + len(s)]:
            if not s:
                self.res.append(' '.join(path))
            else:
                for i in range(1, len(s) + 1):
                    if s[:i] in self.wordDict:
                        self.backtrack(s[i:], idx + i, path+[s[:i]])

    def isWordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j]  and s[j:i] in wordDict:
                    dp[i] = True
        return dp
# @lc code=end
