#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dqMax, dqMin = collections.deque(), collections.deque()
        res = l = 0

        for r in range(len(nums)):
            while dqMax and nums[dqMax[-1]] <= nums[r]:
                dqMax.pop()
            while dqMin and nums[dqMin[-1]] >= nums[r]:
                dqMin.pop()

            dqMax.append(r)
            dqMin.append(r)

            while nums[dqMax[0]] - nums[dqMin[0]] > limit:
                l += 1
                if dqMax[0] < l:
                    dqMax.popleft()
                if dqMin[0] <l:
                    dqMin.popleft()
            res = max(res, r - l + 1)
        return res

# @lc code=end
