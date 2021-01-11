#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            word1, word2 = words[i- 1], words[i]
            n1, n2 = len(word1), len(word2)
            for j in range(min(n1, n2)):
                if word1[j] == word2[j]:
                    continue
                if dic[word1[j]] > dic[word2[j]]:
                    return False
                else:
                    break
            if n1 > n2 and word1[:n2] ==  word2:
                return False
        return True
# @lc code=end
