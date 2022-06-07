#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        slow, fast = 0, 0
        d = collections.defaultdict()
        s_list = list(s)
        p_list = list(p)
        d2 = collections.defaultdict()
        for i in range(len(p_list)):
            d2[p_list[i]] = d2.get(p_list[i], 0) + 1
        counter = len(d2)
        while fast < len(s):
            c = s_list[fast]
            if c in d2:
                d2[c] -= 1
                if d2[c] == 0:
                    counter -= 1
            fast += 1

            while counter == 0:
                tempc = s_list[slow]
                if tempc in d2:
                    d2[tempc] += 1
                    if d2[tempc] > 0:
                        counter += 1
                if fast - slow == len(p):
                    res.append(slow)
                slow += 1
        return res
# @lc code=end
