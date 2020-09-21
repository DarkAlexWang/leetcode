#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return
        result = []
        self.dfs(n, 0, 0, '', result)
        return result

    def dfs(self, n, left, right, path, result):
        if left + right == 2 * n:
            result.append(path)
        # left and right mean used parenthese
        if left < n:
            path += '('
            self.dfs(n, left + 1, right, path, result)
            path = path[:-1]
            print('( is this', path)
        if right < left:
            path += ')'
            self.dfs(n, left, right +1, path, result)
            path = path[:-1]
            print(') is this', path)

# @lc code=end
