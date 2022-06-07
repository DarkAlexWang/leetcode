#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        slow, fast = 0, 0
        counter = 0
        res = 0
        dic = collections.defaultdict()
        while fast < len(s):
            dic[s[fast]] = dic.get(s[fast], 0) + 1
            if dic[s[fast]] == 1:
                counter += 1
            fast += 1

            while counter > 2:
                dic[s[slow]] -= 1
                if dic[s[slow]] == 0:
                    counter -= 1
                slow += 1
            res = max(res, fast - slow)
        return res

# @lc code=end
