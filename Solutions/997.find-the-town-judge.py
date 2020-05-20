#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        arr = [0] * (N + 1)
        for (a, b) in trust:
            arr[a] -= 1
            arr[b] += 1
        for i in range(1, len(arr)):
            if arr[i]  == N-1:
                return i
        return -1
# @lc code=end
