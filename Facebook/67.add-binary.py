#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''

        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res += str(carry % 2)
            carry //= 2
        return res[::-1]
# @lc code=end
