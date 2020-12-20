#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if board is None or board[0] is None:
            return 0
        res, m, n = 0, len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and not visited[i][j]:
                    res += 1
                    q = collections.deque([(i, j)])
                    print(q)
                    while q:
                        t0, t1 = q.popleft()
                        visited[t0][t1] = True
                        for d in dirs:
                            x = t0 + d[0]
                            y = t1 + d[1]
                            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or board[x][y] == '.':
                                continue
                            q.append((x, y))
        return res

# @lc code=end
