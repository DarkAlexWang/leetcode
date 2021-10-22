#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        r1 = any(matrix[0][j] == 0 for j in range(m))
        c1 = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] * matrix[0][j] == 0:
                    matrix[i][j] = 0
        if r1:
            for i in range(m):
                matrix[0][i] = 0
        if c1:
            for j in range(n):
                matrix[j][0] = 0
# @lc code=end
