#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        n = len(nums)
        res = []
        if n == 0:
            self.add(res, lower -1, upper + 1)
            return res
        self.add(res, lower - 1, nums[0])
        for i in range(1, n):
            self.add(res, nums[i - 1], nums[i])
        self.add(res, nums[n - 1], upper + 1)
        return res

    def add(self, res, lower, upper):
        if lower == upper:
            return
        elif lower + 1 == upper:
            return
        elif lower + 1 == upper - 1:
            res.append(str(lower + 1))
        else:
            res.append(str(lower + 1) + "->" + str(upper - 1))

# @lc code=end
