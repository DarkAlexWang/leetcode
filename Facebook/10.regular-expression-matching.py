# @lc lang=python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        return self.is_match(s, p, 0, 0, memo)

    def is_match(self, s, p, i, j, memo):
        if j == len(p):
            return i == len(s)
        if memo[i][j] != False:
            return memo[i][j]

        if j + 1 < len(p) and p[j + 1] == "*":
            memo[i][j] = (self.is_match(s, p, i, j + 2, memo) or (self.iscurrentlettermatch(s, p, i, j) and self.is_match(s, p, i + 1, j, memo)))
        else:
            memo[i][j] = self.iscurrentlettermatch(s, p, i, j) and self.is_match(s, p , i + 1, j + 1, memo)

        return memo[i][j]

    def iscurrentlettermatch(self, s, p, i, j):
        return i < len(s) and (s[i]  == p[j] or  p[j] == '.')
