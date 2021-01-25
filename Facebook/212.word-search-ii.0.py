#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        does_exist = False
        for word in words:
            does_exist = self.exist(board, word)
            if does_exist:
                res.append(word)
        return res

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
        return False

    def dfs(self, board, i, j, count, word):
        if count == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
            return False

        tmp = board[i][j]

        board[i][j] = '  '
        found = self.dfs(board, i + 1, j, count + 1, word) or \
                self.dfs(board, i - 1, j, count + 1, word) or \
                self.dfs(board, i, j - 1, count + 1, word) or \
                self.dfs(board, i, j + 1, count + 1, word)
        board[i][j] = tmp
        return found

# @lc code=end
