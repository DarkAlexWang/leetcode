import collections
class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c

class Solution:
    def is_safe(self, grid, r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 0

    def min_steps(self, grid):
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = collections.deque()
        init_point = Point(0, 0)
        q.append(init_point)
        grid[0][0] = 0 # mark as visited
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
                        if grid[r][c] == 9:
                            return steps
                        grid[r][c] = 0
                        q.append(Point(r, c))
                sz -= 1
            steps += 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    #ans = solution.min_steps([[1, 0, 0], [1, 0, 0], [1, 9, 1]])
    ans = solution.min_steps([[1, 1, 0, 1], [1, 0, 0, 9], [1, 1, 1, 1]])
    print(ans)
