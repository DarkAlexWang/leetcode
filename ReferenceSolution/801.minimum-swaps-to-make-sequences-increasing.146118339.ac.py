#
# [819] Minimum Swaps To Make Sequences Increasing
#
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
#
# algorithms
# Medium (18.83%)
# Total Accepted:    1.1K
# Total Submissions: 5.9K
# Testcase Example:  '[1,3,5,4]\n[1,2,3,7]'
#
# We have two integer sequences A and B of the same non-zero length.
# 
# We are allowed to swap elements A[i] and B[i].  Note that both elements are
# in the same index position in their respective sequences.
# 
# At the end of some number of swaps, A and B are both strictly increasing.  (A
# sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... <
# A[A.length - 1].)
# 
# Given A and B, return the minimum number of swaps to make both sequences
# strictly increasing.  It is guaranteed that the given input always makes it
# possible.
# 
# 
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
# 
# 
# Note:
# 
# 
# A, B are arrays with the same length, and that length will be in the range
# [1, 1000].
# A[i], B[i] are integer values in the range [0, 2000].
# 
#
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        pre = [0, 1]
        for i in range(1, n):
            cur = [sys.maxsize, sys.maxsize]
            if A[i]>A[i-1] and B[i]>B[i-1]:
                cur[0] = min(cur[0], pre[0])
                cur[1] = min(cur[1], pre[1]+1)
            if A[i]>B[i-1] and B[i]>A[i-1]:
                cur[0] = min(cur[0], pre[1])
                cur[1] = min(cur[1], pre[0]+1)
            pre = cur
        return min(pre)
        
