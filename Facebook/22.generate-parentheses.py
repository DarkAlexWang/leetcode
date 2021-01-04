#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        self.dfs(n, 0, 0, '', res)
        return res
    def dfs(self, n, left, right, path, res):
        if left + right == 2 * n:
            res.append(path)

        if left < n:
            path += '('
            self.dfs(n, left+1, right, path, res)
            path = path[:-1]
        if right < left:
            path += ')'
            self.dfs(n, left, right + 1, path, res)

# @lc code=end
