#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        def dfs(jobs, d):
            if d == 1:
                return max(jobs)
            minDiff = float('inf')
            for i in range(1, len(jobs)):
                curr = max(jobs[:i]) + dfs(jobs[i:], d - 1)
                minDiff = min(minDiff, curr)
            return minDiff
        return dfs(jobDifficulty, d)
# @lc code=end
