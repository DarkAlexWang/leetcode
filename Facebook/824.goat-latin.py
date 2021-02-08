#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set('aeiouAEIOU')
        words = S.split()
        for i in range(len(words)):
            if words[i][0] in vowel:
                words[i] = words[i] + 'ma' + 'a' * (i + 1)
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma' + 'a' * (i + 1)
        return " ".join(words)
# @lc code=end
