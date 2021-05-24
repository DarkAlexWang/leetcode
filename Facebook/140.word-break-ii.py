# @lc lang=python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, set(wordDict), {})

    def dfs(self, s, d, m):
        if s in m:
            return m[s]
        if not s:
            return [""]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] in d:
                for word in self.dfs(s[i:], d, m):
                    res.append(s[:i] + (" " if word else "") +  word)
        m[s] = res
        return res
