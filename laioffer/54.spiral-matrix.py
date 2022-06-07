#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        recursiveTraverse(matrix, 0, len(matrix), res)
        return res
        def recursiveTraverse(matrix, offset, size, res):
            if size == 0:
                return
            if size == 1:
                res.append(matrix[offset][offset])
                return
            for i in range(size - 1):
                res.append(matrix[offset][offset + i])
            for i in range(size - 1):
                res.append(matrix[offset + i][offset + size - 1])
            for i in range(size - 1, 1, -1):
                res.append(matrix[offset + size - 1][offset + i])
            for i in range(size - 1, 1, -1):
                res.append(matrix[offset + i][offset])
            recursiveTraverse(matrix, offset + 1, size - 2, res)

# @lc code=end
