#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_A = len(A)
        len_B = len(B)
        ans = [[0 for i in range(len_B + 1)] for j in range(len_A + 1)]
        for i in range(len_A):
            for j in range(len_B):
                if A[i] == B[j]:
                    ans[i +1][j +1] = ans[i][j] + 1
                else:
                    ans[i+1][j+1] = max(ans[i+1][j], ans[i][j+1])
        return ans[i+1][j+ 1]

# @lc code=end
