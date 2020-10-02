#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p = p //10
        return res == x
# @lc code=end
