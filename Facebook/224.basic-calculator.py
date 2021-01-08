# @lc lang=python3
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10 * num + int(ss)
            elif ss in ['-', '+']:
                res += sign * num
                num = 0
                sign = 1 if ss == '+' else -1
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign
