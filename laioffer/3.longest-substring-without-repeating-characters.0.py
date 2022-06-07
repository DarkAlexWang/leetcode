#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        res, counter = 0, 0
        dic = collections.defaultdict()
        while fast < len(s):
            dic[s[fast]] = dic.get(s[fast], 0) + 1
            if dic[s[fast]] > 1:
                counter += 1
            fast += 1
            while counter > 0:
                if dic[s[slow]] > 1:
                    counter -= 1
                dic[s[slow]] -= 1
                slow += 1
            res = max(res, fast - slow)
        return res
# @lc code=end
