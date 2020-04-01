#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n <= 0 and k <= 0:
            return res
        self.helper(n,k, 1, res, [])
        return res

    def helper(self, n, k, start, res, path):
        if k == 0:
            res.append(path[:])
        else:
            for i in list(range(start, n+1)):
                path.append(i)
                self.helper(n, k-1, i+1, res, path)
                path.pop()
# @lc code=end
