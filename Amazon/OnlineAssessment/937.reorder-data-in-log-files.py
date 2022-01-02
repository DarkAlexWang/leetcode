#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[0])
        # sort by suffix
        letters.sort(key = lambda x: x.split()[1:])

        # put digit logs after letter logs
        res = letters + digits
        return res
# @lc code=end
