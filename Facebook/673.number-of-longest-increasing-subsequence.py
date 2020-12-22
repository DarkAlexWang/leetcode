#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #dp, longest = [[1, 1] for i in range(len(nums))], 1
        #for i, num in enumerate(nums):
        #    curr_longest, count = 1, 0
        #    for j in range(i):
        #        if nums[j] < num:
        #            curr_longest = max(curr_longest, dp[j][0] + 1)
        #    for j in range(i):
        #        if dp[j][0] == curr_longest - 1 and nums[j] < num:
        #            count += dp[j][1]
        #    dp[i] = [curr_longest, max(count, dp[i][1])]
        #    longest = max(curr_longest, longest)
        #return sum([item[1] for item in dp if item[0] == longest])

        res, mx, n = 0, 0, len(nums)
        length, cnt = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if length[i] == length[j] + 1:
                    cnt[i] += cnt[j]
                elif length[i] < length[j] + 1:
                    length[i] = length[j] + 1
                    cnt[i] = cnt[j]
            if mx == length[i]:
                res += cnt[i]
            elif mx< length[i]:
                mx = length[i]
                res = cnt[i]
        return res

# @lc code=end
