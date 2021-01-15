class TrieNode:
    def TrieNode(self, head):
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, 0, word, visited)
                return True
        return False

    def dfs(self, i, j, idx, word, visited):
        m, n = len(board), len(board[0])
        if idx == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[idx]:
            return False

        visited[i][j] = True
        res = self.dfs(i + 1, j, idx + 1, word, visited)  or self.dfs(i - 1, j, idx + 1, word, visited) or self.dfs(i, j + 1, idx + 1, word, visited) or self.dfs(i, j - 1, idx + 1, word, visited)
        visited[i][j] = False

        return res
