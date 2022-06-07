#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_list = list(s)
        t_list = list(t)
        if len(s) < len(t):
            return ""
        dic = collections.defaultdict()
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        counter = len(dic)
        fast, slow = 0, 0
        head = 0
        res_len = sys.maxsize
        while fast < len(s):
            if s[fast] in dic:
                dic[s[fast]] -= 1
                if dic[s[fast]] == 0:
                    counter -= 1
            fast += 1

            while counter == 0:
                if s[slow] in dic:
                    dic[s[slow]] += 1
                    if dic[s[slow]] > 0:
                        counter += 1
                if fast - slow < res_len:
                    res_len = fast - slow
                    head = slow

                slow += 1
        if res_len == sys.maxsize:
            return ""
        return "".join(s[head: head + res_len])

# @lc code=end
