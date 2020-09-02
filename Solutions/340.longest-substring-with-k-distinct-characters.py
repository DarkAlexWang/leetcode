class Solution:
    def lengthOfLongestSubstringKDistinct(self, s):
        res = left = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i], 0) + 1
            while len(dict) > k:
                dict[s[i]] -= 1
                if dict[s[i]] == 0:
                    del dict[s[i]]
                    left += 1
            res = max(res, i - start + 1)
        return res
