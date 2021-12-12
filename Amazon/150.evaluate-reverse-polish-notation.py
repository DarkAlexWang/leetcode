#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        for s in tokens:
            if s in "+-*/":
                b = q.pop()
                a = q.pop()
                if s == "+":
                    q.append(a + b)
                if s == "-":
                    q.append(a - b)
                if s == "*":
                    q.append(a * b)
                if s == "/":
                    q.append(int(operator.truediv(a, b)))

            else:
                q.append(int(s))
        return q[0]

# @lc code=end
