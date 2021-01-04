#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res

    def dfs(self, digits, dic, idx, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(idx, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i + 1, path + j, res)
# @lc code=end
