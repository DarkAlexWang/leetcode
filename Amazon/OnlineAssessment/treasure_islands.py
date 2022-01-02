import collections
class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c

class Solution:
    def is_safe(self, grid, r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 'D'

    def min_steps(self, grid):
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = collections.deque()
        init_point = Point(0, 0)
        q.append(init_point)
        grid[0][0] = "D" # mark as visited
        steps = 1
        while q:
            sz = len(q)
            while sz > 0:
                cur = q.popleft()
                p = Point(cur.r, cur.c)
                for d in DIRS:
                    r = p.r + d[0]
                    c = p.c + d[1]
                    if self.is_safe(grid, r, c):
                        if grid[r][c] == 'X':
                            return steps
                        grid[r][c] = 'D'
                        q.append(Point(r, c))
                sz -= 1
            steps += 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    ans = solution.min_steps([['0', '0', '0', '0'], ['D', '0', 'D', '0'], ['0', '0', '0', '0'], ['X', 'D', 'D', '0']])
    print(ans)
