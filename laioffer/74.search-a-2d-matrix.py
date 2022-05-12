#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                b = mid - 1
            else:
                t = mid + 1
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[b][mid] == target:
                return True
            elif matrix[b][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

# @lc code=end
