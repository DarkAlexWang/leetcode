import sys
class Solution:
    def max_min_path(self, matrix):
        row, col = len(matrix), len(matrix[0])
        self.max_value, min_value = -sys.maxsize, sys.maxsize
        self.dfs(matrix, min_value, 0, 0)
        return self.max_value

    def dfs(self, matrix, min_value, i, j):
        row, col = len(matrix), len(matrix[0])
        if i >= row or j >= col:
            return
        if i == row - 1 and j == col - 1:
            min_value = min(min_value, matrix[i][j])
            self.max_value = max(self.max_value, min_value)
            return
        min_value = min(min_value, matrix[i][j])
        self.dfs(matrix, min_value, i, j +1)
        self.dfs(matrix, min_value, i + 1, j)

if __name__ == '__main__':
    solution = Solution()
    matrix = [[8, 4, 7], [6, 5, 9]]
    res = solution.max_min_path(matrix)
    print(res)
