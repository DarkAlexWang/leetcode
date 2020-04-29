#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        l = len(p)
        ans =[]
        hashp =  [0] * 123
        hashs = [0] * 123
        for char in p:
            hashp[ord(char) - ord('a')] += 1
        for i in range(n):
            if i >= l:
                hashs[ord(s[i - l]) - ord('a')] -= 1
            hashs[ord(s[i]) - ord('a')] += 1
            if hashp == hashs:
                ans.append(i + 1 -l)
        return ans

# @lc code=end
