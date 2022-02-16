#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_word = s.split(' ')
        if len(pattern) != len(split_word):
            return False
        if len(pattern) == 0 and len(split_word) == 0:
            return True
        if len(set(pattern)) != len(set(split_word)):
            return False

        dic = {}
        for p, word in zip(pattern, split_word):
            if word in dic:
                if dic[word] != p:
                    print(dic)
                    return False
                else:
                    continue
            else:
                dic[word] = p
        return True


# @lc code=end
