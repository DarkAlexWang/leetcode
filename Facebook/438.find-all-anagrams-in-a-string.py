#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashs = [0] * 26
        hashp = [0] * 26
        n = len(p)
        res = []
        for char in p:
            hashp[ord(char) - ord('a')] += 1
        for i in range(len(s)):
            if i >= n:
                hashs[ord(s[i - n]) - ord('a')] -= 1
            hashs[ord(s[i]) - ord('a')] += 1
            if hashs == hashp:
                res.append(i - n + 1)
        return res

# @lc code=end
