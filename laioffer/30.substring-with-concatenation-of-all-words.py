#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return res
        dic = collections.defaultdict()
        cur_dic = collections.defaultdict()
        for word in words:
            dic[word] = dic.get(word, 1) + 1
        string = ""
        tmp = ""
        for i in range(len(words[0])):
            count = 0
            start = i
            for r in range(i, len(s) + 1, len(words[0])):
                string = s[r:r + len(words[0])]
                if string in dic:
                    cur_dic[string] = cur_dic.get(string, 1) + 1
                if cur_dic[string] <= dic[string]:
                    count += 1
                while cur_dic[string] > dic[string]:
                    tmp = s[start, start + len(words[0])]
                    cur_dic[tmp] -= 1
                    start += len(words[0])

                    if cur_dic[tmp] < dic[tmp]:
                        count -= 1
                if count == len(words):
                    res.append(start)
                    tmp = s[start: start+ len(words[0])]
                    cur_dic[tmp] -= 1
                    start += len(words[0])
                    count -= 1
                else:
                    cur_dic = {}
                    count = 0
                    start = r + len(words[0])
            cur_dic = {}
        return res

# @lc code=end
