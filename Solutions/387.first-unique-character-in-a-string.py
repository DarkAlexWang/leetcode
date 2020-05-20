#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        firstUniqe = {}
        for idx, num in enumerate(s):
            if num not in firstUniqe:
                firstUniqe[num] = idx
            else:
                firstUniqe[num] = -1
        for k, v in firstUniqe.items():
            if v != -1:
                return v
        return -1


# @lc code=end
