# @lc lang=python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        res = ""
        dic = collections.defaultdict()

        #init
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        l, r = 0, 0
        minLength = len(s)

        size = len(t)

        while r < len(s):
            if s[r] in dic:
                if dic[s[r]] >0:
                    size -= 1
                dic[s[r]] -= 1
            r += 1

            #left bound
            while size == 0:
                if minLength >= r - l:
                    minLength = r - l
                    res = s[l: r]

                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        size += 1
                l += 1
        return res
