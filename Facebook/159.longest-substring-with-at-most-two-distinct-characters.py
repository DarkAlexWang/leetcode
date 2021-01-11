#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        freq = collections.Counter()
        res = 0
        for end, ch in enumerate(s):
            freq[ch] += 1
            while len(freq) > 2:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
            res = max(res, end - start + 1)
        return res

# @lc code=end
