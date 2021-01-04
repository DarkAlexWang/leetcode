#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = collections.deque()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float('inf')

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            x, y = q.popleft()

            for i, j in dirs:
                row = x + i
                col = y + j
                if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] > 1 + matrix[x][y]:
                    matrix[row][col] = matrix[x][y] + 1
                    q.append((row, col))
        return matrix
# @lc code=end
