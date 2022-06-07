#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = []
        self.helper(n, cur, res)
        return res

    def helper(self, n, cur, res):
        if len(cur) == n:
            res.append(cur)
            return
        for i in range(n):
            if self.valid(cur, i):
                cur.append(i)
                self.helper(n, cur, res)
                #cur.pop(len(cur) - 1)

    def valid(self, cur, column):
        row = len(cur)
        for i in range(row):
            if cur[i] == column or abs(cur[i] - column) == row - i:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    ans = solution.solveNQueens(3)
    print(ans)
# @lc code=end
