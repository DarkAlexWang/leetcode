#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = collections.deque()
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    q.append((row, col))
        dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
        while q:
            i, j = q.popleft()
            for x, y in dirs:
                row = i + x
                col = j + y
                if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] == 2147483647:
                    rooms[row][col] = rooms[i][j] + 1
                    q.append((row, col))
# @lc code=end
