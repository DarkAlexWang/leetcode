# @lc lang=python3
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        n, m, k = len(A), len(A[0]), len(B[0])
        row_vector = [[(j, A[i][j]) for j in range(m) if A[i][j] != 0] for i in range(n)]
        col_vector = [[(i, B[i][j]) for i in range(m) if B[i][j] != 0] for j in range(k)]

        C = [[self.multi(row, col) for col in col_vector] for row in row_vector]
        return C
    def multi(self, row, col):
        res = 0
        i = 0
        for j in range(len(col)):
            while i < len(row) and row[i][0] < col[j][0]:
                i += 1
            if i < len(row) and row[i][0] == col[j][0]:
                res += row[i][1] * col[j][1]
        return res
