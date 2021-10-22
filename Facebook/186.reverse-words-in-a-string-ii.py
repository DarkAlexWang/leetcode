#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)

        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i - 1)
                beg = i + 1
            elif i == len(s) - 1:
                self.reverse(s, beg, i)
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

# @lc code=end
