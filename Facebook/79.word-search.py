# @lc app=leetcode lang=python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, i, j, visited):
                    return True
        return False

    def dfs(self, board, word, idx, i, j, visited):
        if idx == len(word):
            return True
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or board[i][j] != word[idx]:
            return False
        visited[i][j] = True
        res = self.dfs(board, word, idx + 1, i - 1, j, visited) \
              or self.dfs(board, word, idx + 1, i + 1, j, visited) \
              or self.dfs(board, word, idx + 1, i, j - 1, visited) \
              or self.dfs(board, word, idx + 1, i, j + 1, visited)

        visited[i][j] = False
        return res
