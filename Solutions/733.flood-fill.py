#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        def dfs(i, j):
            if i >= row or i < 0 or j >= col or j < 0:
                return
            if image[i][j] == newColor or image[i][j] != color:
                return
            image[i][j] = newColor
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        dfs(sr, sc)
        return image
# @lc code=end
