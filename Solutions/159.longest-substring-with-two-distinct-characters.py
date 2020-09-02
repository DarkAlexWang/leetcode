class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        res = left = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i], 0) + 1
            while len(dict) > 2:
                dict[s[left]] -= 1
                if dict[s[left]] == 0:
                    del dict[s[left]]
                    left -= 1
            res = max(res, i - left + 1)

        return res
