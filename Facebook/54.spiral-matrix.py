# @lc app=leetcode id=54 lang=python3
#
# [54] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res

        row_begin = 0
        row_end = len(matrix) - 1
        col_begin = 0
        col_end = len(matrix[0]) - 1

        while row_begin <= row_end and col_begin <= col_end:
            for j in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][j])
            row_begin += 1

            for j in range(row_begin, row_end + 1):
                res.append(matrix[j][col_end])
            col_end -= 1

            if row_begin <= row_end:
                for j in range(col_end, col_begin - 1, -1):
                    res.append(matrix[row_end][j])
            row_end -= 1

            if col_begin <= col_end:
                for j in range(row_end, row_begin - 1, -1):
                    res.append(matrix[j][col_begin])
            col_begin +=  1
        return res
# @lc code=end
