#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        q1 = collections.deque()
        q2 = collections.deque()
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            q1.append((i, 0))
            q2.append((i, n -1))
            pacific[i][0] = True
            atlantic[i][n - 1] = True
        for i in range(n):
            q1.append((0, i))
            q2.append((m - 1, i))
            pacific[0][i] = True
            atlantic[m -1][i] = True

        self.bfs(matrix, pacific, q1)
        self.bfs(matrix, atlantic, q2)
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append((i, j))

        return res

    def bfs(self, matrix, visited, queue):
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        while queue:
            t = queue.popleft()
            for d in dirs:
                x = t[0] + d[0]
                y = t[1] + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or \
                visited[x][y] or matrix[x][y] < matrix[t[0]][t[1]]:
                    continue
                visited[x][y] = True
                queue.append((x, y))


# @lc code=end
