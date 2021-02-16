#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {"0":"0", "1":"1", "6":"9", "9": "6"}
        l, r= 0, len(num) - 1
        while l <= r:
            if num[l] not in dic or dic[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

# @lc code=end
