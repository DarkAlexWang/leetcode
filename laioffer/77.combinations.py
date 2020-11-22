#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res
    def dfs(self, n, k, start, path, res):
        if k == 0:
            res.append(path.copy())
            return
        for i in range(start, n + 1):

            path.append(i)
            self.dfs(n, k - 1, i + 1, path, res)
            path.pop()
# @lc code=end
