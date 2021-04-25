#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[index][diff] equals to the length of arithmetic sequence at index
        # with difference
        # Time O(N^2)
        # Space O(N^2)
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
# @lc code=end
