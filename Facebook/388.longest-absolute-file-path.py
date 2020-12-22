#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dic = {}
        longest = 0
        file_list = input.split("\n")
        for i in file_list:
            if "." not in i:
                key = i.count("\t")
                value = len(i.replace("\t", ""))
                dic[key] = value
            else:
                key = i.count("\t")
                length = sum([dic[j] for j in dic.keys() if j < key]) + len(i.replace("\t", "")) + key
                longest =  max(longest, length)
        return longest
# @lc code=end
