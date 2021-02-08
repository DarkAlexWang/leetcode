#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_digit = False
        met_dot = False
        met_e = False
        for i in range(len(s)):
            if s[i] in ["+", "-"]:
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif s[i] == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif s[i] == 'e' or s[i] == 'E':
                if met_e or not met_digit:
                    return False
                met_e = True
                met_digit = False
            elif s[i].isdigit():
                met_digit = True
            else:
                return False
        return met_digit

# @lc code=end
