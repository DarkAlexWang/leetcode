#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0] or start == destination:
            return 0
        m, n = len(maze), len(maze[0])
        visited = {(start[0], start[1]): 0}
        queue = collections.deque([(start[0], start[1], 0)])

        while queue:
            i, j, dist = queue.popleft()

            dic = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in dic:
                x, y, d = i, j, dist
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x+dx][y + dy]== 0:
                    x += dx
                    y += dy
                    d += 1
                if (x, y) not in visited or ((x,  y) in visited and visited[(x, y)] > d):
                    visited[(x, y)] = d
                    if (x, y) != (destination[0], destination[1]):
                        queue.append((x,y, d))
        return visited.get((destination[0], destination[1]), -1)
# @lc code=end
