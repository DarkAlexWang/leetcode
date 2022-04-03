#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        bcount = 0
        for l in s:
            if l == 'a':
                # either remove this 'a': res + 1
                # or keep this 'a': bcount (must remove all previous 'b')
                res = min(res + 1, bcount)
            else:
                bcount += 1
        return res
# @lc code=end
