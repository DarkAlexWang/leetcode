#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        front, back = [], set()

        for i, c in enumerate(s):
            if c == '(':
                front.append(i)
            elif c == ')':
                if front:
                    front.pop()
                else:
                    back.add(i)
        for i in front:
            back.add(i)

        return "".join([c for i, c in enumerate(s) if i not in back])
# @lc code=end
