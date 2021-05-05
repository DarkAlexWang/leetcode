#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        s = list(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                one, two = s[l:r], s[l + 1: r + 1]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1
        return True
# @lc code=end
