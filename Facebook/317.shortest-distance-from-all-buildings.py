#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#

# @lc code=start
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        buildings = sum(val for line in grid for val in line if val == 1)

        hit, distSum = [[0] * n for i in range(m)], [[0] * n for i in range(m)]

        def bfs(start_x, start_y):
            visited = [[False] * n for k in range(m)]
            visited[start_x][start_y], count1, q = True, 1, collections.deque([(start_x, start_y, 0)])

            while q:
                x, y, dist = q.popleft()
                for i, j in ((x + 1, y), (x -1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            q.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    if not bfs(x, y):
                        return -1
        return min([distSum[i][j] for i in range(m) for j in range(n) if not grid[i][j] and hit[i][j] == buildings] or [-1])
# @lc code=end
