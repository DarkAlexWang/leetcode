#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

# @lc code=start
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for string in strings:
            code = self.encode(string)
            dic[code].append(string)
        return list(dic.values())

    def encode(self, string):
        if len(string) == 0:
            return -1
        elif len(string) == 1:
            return 1
        code = [0] * (len(string) - 1)
        for i in range(1, len(string)):
            code[i - 1] = (ord(string[i]) - ord(string[i - 1])) % 26
        return tuple(code)
# @lc code=end
