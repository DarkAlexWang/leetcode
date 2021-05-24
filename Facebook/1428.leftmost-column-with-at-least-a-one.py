# @lc lang=python3
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        mostleft = -1
        l, r = 0, n - 1
        while l < m and r >= 0:
            if binaryMatrix.get(l, r):
                mostleft = r
                r -= 1
            else:
                l += 1
        return mostleft
