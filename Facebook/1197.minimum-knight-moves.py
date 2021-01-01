# @lc lang=python3
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        return self.bfs(0, 0, abs(x), abs(y))

    def bfs(self, i, j, x, y):
        open_list = collections.deque([(i, j, 0)])
        seen = {(i, j)}
        while open_list:
            i, j, d = open_list.popleft()
            for di, dj in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]:
                r, c = i + di, j + dj
                if (r, c) not in seen and r > -4 and c > -4:
                    if (r, c) == (x, y):
                        return d + 1
                    seen.add((r, c))
                    open_list.append((r, c, d + 1))
