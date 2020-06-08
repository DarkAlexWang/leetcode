#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)  <= 1:
            return 0
        curMax = 0
        longest = [0] * (len(s))
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i -1] == '(':
                    longest[i] = longest[i-2] + 2 if (i -2) > 0 else 2
                    curMax = max(longest[i], curMax)
                else:
                    if i - longest[i-1] -1 >= 0 and s[i - longest[i-1] -1] == '(':
                        longest[i] = longest[i-1] + 2 + longest[i- longest[i -1] -2] if (i -longest[i-1] -2) >= 0 else longest[i -1] + 2
                        curMax = max(longest[i], curMax)
        return curMax

# @lc code=end
