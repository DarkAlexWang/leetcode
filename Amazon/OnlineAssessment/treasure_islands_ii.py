import collections

class Solution:
    def is_safe(self, grid, r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 'D'

    def shortest_path(self, islands):
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        if len(islands) == 0 or len(islands[0]) == 0:
            return -1
        n = len(islands)
        m = len(islands[0])
        q = collections.deque()
        # add all sources to queue and set "visited"
        steps = 1
        for i in range(n):
            for j in range(m):
                if islands[i][j] == 'S':
                    q.append([i, j])
                    islands[i][j] = 'D'

        while q:
            sz = len(q)
            while sz > 0:
                cur = q.popleft()
                for d in DIRS:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]
                    if self.is_safe(islands, x, y):
                        if islands[x][y] == 'X':
                            return steps
                        islands[x][y] = 'D'
                        q.append([x, y])
                sz -= 1
            steps += 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    ans = solution.shortest_path([['S', 'O', 'O', 'S', 'S'], ['D', 'O', 'D', 'O', 'D'], \
            ['O', 'O', 'O', 'O', 'X'], ['X', 'D', 'D', 'O', 'O'], ['X', 'D', 'D', 'D', 'O']])
    print(ans)
