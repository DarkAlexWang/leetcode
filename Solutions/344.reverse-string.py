#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return
        n = len(s)
        i, j = 0, n -1
        while i < j:
            s[i], s[j] = s[j], s [i]
            i += 1
            j -=1
        return s
# @lc code=end
