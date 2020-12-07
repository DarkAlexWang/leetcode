#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_bracket, right_bracket = 0, 0

        for char in s:
            left_bracket += (char == '(')
            if left_bracket == 0:
                right_bracket += (char == ')')
            else:
                left_bracket -= (char == ')')

        res = []
        self.dfs(s, 0, left_bracket, right_bracket, res)
        return res
    def isValid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def dfs(self, s, start, l, r, res):
        if l == 0 and r == 0:
            if self.isValid(s):
                res.append(s)
            return
        for i in range(start, len(s)):
            if i != start and s[i] == s[i - 1]:
                continue
            if s[i] == '(' or s[i] == ')':
                curr = s[:i] + s[i+1:]
                if r > 0:
                    self.dfs(curr, i, l, r - 1, res)
                elif l > 0:
                    self.dfs(curr, i, l - 1, r, res)
# @lc code=end
