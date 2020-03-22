#
# [795] K-th Symbol in Grammar
#
# https://leetcode.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (36.20%)
# Total Accepted:    4.6K
# Total Submissions: 12.6K
# Testcase Example:  '1\n1'
#
# On the first row, we write a 0. Now in every subsequent row, we look at the
# previous row and replace each occurrence of 0 with 01, and each occurrence of
# 1 with 10.
# 
# Given row N and index K, return the K-th indexed symbol in row N. (The values
# of K are 1-indexed.) (1 indexed).
# 
# 
# Examples:
# Input: N = 1, K = 1
# Output: 0
# 
# Input: N = 2, K = 1
# Output: 0
# 
# Input: N = 2, K = 2
# Output: 1
# 
# Input: N = 4, K = 5
# Output: 1
# 
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# 
# 
# Note:
# 
# 
# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].
# 
#
class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1: return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)/2)
