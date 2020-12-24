class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        visited[start[0]][start[1]] = True

        q = collections.deque([start])

        while q:
            tup = q.popleft()
            if tup[0] == destination[0] and tup[1] == destination[1]:
                return True
            for d in dirs:
                row = tup[0] + d[0]
                col = tup[1] + d[1]

                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
                    row += d[0]
                    col += d[1]

                (new_x, new_y) = (row - d[0], col - d[1])
                if not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
        return False
