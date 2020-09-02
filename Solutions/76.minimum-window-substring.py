#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        res = ""
        dic = dict()
        # init
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        l, r = 0, 0
        minLength = len(s)

        size = len(t)

        while r < len(s):
            if s[r] in dic:
                if dic[s[r]] > 0:
                    size -= 1
                dic[s[r]] -= 1

            r += 1

            while size ==0:
                if minLength >= r -l:
                    minLength = r - l
                    res = s[l:r]

                #left bound
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        size += 1
                l += 1
        return res
# @lc code=end
