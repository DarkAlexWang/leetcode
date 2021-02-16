#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#

# @lc code=start
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9": "6"}
        res = []
        self.helper(res, [None]*n, 0, n - 1, dic)
        return res

    def helper(self, res, item, start, end, dic):
        if start > end:
            res.append("".join(item))
            return
        for key in dic:
            if start == end and key in ('6', '9'):
                continue
            if start != end and start == 0 and key == '0':
                continue
            item[start], item[end] = key, dic[key]
            self.helper(res, item, start + 1, end - 1, dic)
# @lc code=end
