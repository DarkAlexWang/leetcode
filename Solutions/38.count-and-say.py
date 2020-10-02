#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            letter, temp, count = s[0], '', 0
            for l in s:
                if letter == l:
                    count += 1
                else:
                    temp += str(count) + letter
                    letter = l
                    count = 1
            temp += str(count) + letter
            s = temp
        return s
# @lc code=end
