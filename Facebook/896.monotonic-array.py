#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A:
            return False
        if len(A) <= 1:
            return True
        if self.increasing(A) or self.decreasing(A):
            return True
        else:
            return False
    def increasing(self, A):
        for i in range(1, len(A)):
            if A[i] < A[i -1]:
                return False
        return True
    def decreasing(self, A):
        for i in range(1, len(A)):
            if A[i] > A[i -1]:
                return False
        return True
# @lc code=end
