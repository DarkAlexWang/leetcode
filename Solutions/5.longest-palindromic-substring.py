#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n, start, length, maxString = len(s), 0, 1, s[0]
        state = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            state[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(n - 1, i, -1):
                state[i][j] = (s[j] == s[i])
                if j != i + 1:
                    state[i][j] &= state[i+1][j -1]
                if state[i][j] and (j-i +1) > length:
                    length = j-i+1
                    maxString = s[i: j+ 1]
        return  maxString
# @lc code=end
