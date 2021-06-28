#
# @lc app=leetcode id=1763 lang=python3
#
# [1763] Longest Nice Substring
#

# @lc code=start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)  < 2:
            return ""
        chars = set(list(s))
        for i in range(len(s)):
            if not (s[i].lower() in chars and s[i].upper() in chars):
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i + 1:])
                return s2 if len(s2) > len(s1) else s1
        return s
# @lc code=end
