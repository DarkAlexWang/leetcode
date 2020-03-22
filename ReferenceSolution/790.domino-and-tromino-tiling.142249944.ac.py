#
# [806] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (29.32%)
# Total Accepted:    1.1K
# Total Submissions: 3.8K
# Testcase Example:  '3'
#
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
# 
# 
# XX  <- domino
# 
# XX  <- "L" tromino
# X
# 
# 
# Given N, how many ways are there to tile a 2 x N board? Return your answer
# modulo 10^9 + 7.
# 
# (In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.)
# 
# 
# 
# Example:
# Input: 3
# Output: 5
# Explanation: 
# The five different ways are listed below, different letters indicates
# different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
# 
# Note:
# 
# 
# N  will be in range [1, 1000].
# 
# 
# 
# 
#
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        f= [0 for _ in range(1000)]
        f[0],f[1],f[2] = 1,1,2
        for i in range(3,N+1):
            f[i] = 2*f[i-1] + f[i-3]
        return f[N] % (10**9 + 7)
