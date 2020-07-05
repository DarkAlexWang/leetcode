#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or not matrix or (len(matrix[0])) == 0 or target is None:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[m][0]:
                return True
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        row = r
        l, r = 0, len(matrix[row]) -1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        return False
# @lc code=end
